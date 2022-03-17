.PHONY: default

build:
	docker build -t ledmington_website -f website.Dockerfile .

default:
	docker build -t ledmington_website .