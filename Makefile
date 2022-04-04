DC=docker-compose -f docker-compose-dev.yml

.PHONY: serve

build:
	${DC} build

up: build
	${DC} up --remove-orphans

down:
	${DC} down

install:
	bundle install

serve:
	bundle exec jekyll serve --trace --watch

test:
	python3 link_test.py

clean:
	rm -rf build
	rm -rf .jekyll-cache