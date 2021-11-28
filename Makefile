build:
	docker-compose build
run:
	docker-compose up -d
kill:
	docker-compose kill
rm:
	docker-compose kill
	docker-compose rm
restart:
	docker-compose kill 
	docker-compose rm 
	docker-compose up -d
logs:
	docker-compose logs