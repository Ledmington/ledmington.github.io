DC=docker-compose -f docker-compose-prod.yml

.PHONY: serve

up:
	${DC} up --build

down:
	${DC} down

update:
	bundle update

install:
	bundle install

serve:
	bundle exec jekyll serve --trace --livereload --unpublished --draft

clean:
	rm -rf build
	rm -rf .jekyll-cache