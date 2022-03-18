DC=docker-compose -f docker-compose-dev.yml

.PHONY: up build

build:
	${DC} build

up:
	${DC} up

down:
	${DC} down