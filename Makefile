DC=docker-compose -f docker-compose-dev.yml

.PHONY: build

build:
	${DC} build

up:
	${DC} up --remove-orphans

down:
	${DC} down

clean:
	rm -rf build
	rm -rf .jekyll-cache