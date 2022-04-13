DC=docker-compose -f docker-compose-dev.yml

.PHONY: serve

build:
	${DC} build

up: build
	${DC} up --remove-orphans

down:
	${DC} down

update:
	rm requirements.txt
	pipreqs
	bundle update

install:
	pip install -r requirements.txt
	bundle install

serve:
	bundle exec jekyll serve --trace --watch --unpublished --draft

test:
	python3 link_test.py
	python3 html_validator.py

clean:
	rm -rf build
	rm -rf .jekyll-cache