docker/build:
	docker build -t doctor-availability .
docker/run:
	docker run --name check-docs --restart always doctor-availability
docker/kill:
	docker kill check-docs
docker/rm:
	docker rm check-docs