DC=docker-compose -f docker-compose-dev.yml

.PHONY: serve

build:
	${DC} build

up: build
	${DC} up --remove-orphans

down:
	${DC} down

install:
	bundle update
	bundle install

serve:
	bundle exec jekyll serve --trace --incremental --watch --livereload

clean:
	rm -rf build
	rm -rf .jekyll-cache