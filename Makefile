network_name = microservices
image_name = vault

all: create_network build_image
	@ docker run --name vault --network microservices -p 8200:8200 -v secret_volume:/vault/file --cap-add IPC_LOCK -e VAULT_ADDR=http://127.0.0.1:8200 -d vault
	@ docker compose -f ./services/docker-compose.yml up -d --build

create_network:
	@ if [ -z "$$(docker network ls | grep $(network_name))" ]; then \
		docker network create -d bridge $(network_name); \
	fi

build_image:
	@ if [ -z "$$(docker images | grep -w $(image_name))" ]; then \
		docker build -t $(image_name) ./services/vault/; \
	fi

down:
	@ docker compose -f ./services/docker-compose.yml down
	@ docker stop vault
	@ docker rm vault


re: down all

clean:
	@docker stop $$(docker ps -qa);\
	 docker rm $$(docker ps -qa);\
	 docker rmi -f $$(docker images -qa);\
	 docker volume rm $$(docker volume ls -q);\
	 docker network rm $$(docker network ls -q);
 
.PHONY: all re down clean create_network build_image
