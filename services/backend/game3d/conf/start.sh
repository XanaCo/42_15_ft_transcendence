#!/bin/bash

sh /tmp/init_db.sh
service postgresql start

sleep 5
python3 manage.py makemigrations

sleep 5
python3 manage.py migrate

# python3 manage.py createsuperuser --noinput # create superuser for admin

sleep 5

data=$(curl -H "X-Vault-Token: $(cat /tmp/.key)" http://vault:8200/v1/kv/nginx | jq -r '.data'| sed 's/\\n/\\\\n/g')
echo $data

ssl_certificate=$(echo $data | jq -r '.ssl_certificate')
ssl_certificate_key=$(echo $data | jq -r '.ssl_certificate_key')

echo "$ssl_certificate" > /tmp/server.crt
echo "$ssl_certificate_key" > /tmp/server.key

cp /tmp/server.crt /usr/local/share/ca-certificates/
update-ca-certificates
openssl x509 -in /usr/local/share/ca-certificates/server.crt -out /usr/local/share/ca-certificates/server.pem -outform PEM

gunicorn --certfile=/tmp/server.crt --keyfile=/tmp/server.key game3d.wsgi:application --bind 0.0.0.0:4430
