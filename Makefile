DC=docker-compose -f docker-compose-dev.yml

.PHONY: serve

build:
	${DC} build

up: build
	${DC} up --remove-orphans

down:
	${DC} down

serve:
	bundle update
	bundle install
	bundle exec jekyll serve --watch

clean:
	rm -rf build
	rm -rf .jekyll-cache