#!/bin/bash

sh /tmp/init_db.sh
service postgresql start

sleep 5

python3 manage.py makemigrations arena


sleep 5

python3 manage.py migrate
python3 /app/setupDataBase.py

sleep 5
python3 manage.py runserver 0.0.0.0:8080
