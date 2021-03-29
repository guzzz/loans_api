#!/bin/bash
.PHONY: default
.SILENT:


default:

shell:
	docker-compose stop api
	docker-compose run --rm --service-ports api bash

createsuperuserfast:
	docker-compose run --rm api python manage.py createsuperuserfast --password loans1234 --noinput --email 'admin@email.com'

createsuperuser:
	docker-compose run --rm api python manage.py createsuperuser

migrations:
	docker-compose run --rm api python manage.py makemigrations

migrate:
	docker-compose run --rm api python manage.py migrate --noinput

start:
	docker-compose up -d

start_api:
	docker-compose run --rm --service-ports api

stop:
	docker-compose down

collectstatic:
	docker-compose run --rm api python manage.py collectstatic --noinput

build:
	docker-compose build --force-rm --no-cache --pull
	make collectstatic
	make tests

setup:
	docker network create loans_net
	docker-compose build --force-rm --no-cache --pull
	make migrations
	make migrate
	make collectstatic
	make createsuperuserfast
	make collectstatic
	make tests

logs:
	docker-compose logs --follow

tests:
	docker-compose run --rm api python manage.py test

clean:
	make stop
	docker image rm $$(docker image ls -q -f reference=loans_django_api)
	docker volume rm $$(docker volume ls -q -f name=loans)
	docker network rm loans_net

startapp:
	docker-compose stop api
	docker-compose run --rm api python manage.py startapp $(app)
	mv -f $(app) loans_api/
	touch loans_api/$(app)/serializers.py
	touch loans_api/$(app)/choices.py
	touch loans_api/$(app)/routers.py
	touch loans_api/$(app)/services.py

coverage:
	docker-compose -f docker-compose.yml run --rm --service-ports api bash -c \
	"coverage run --source='.' manage.py test; \
	coverage report --rcfile=.coveragerc; \
	coverage html --rcfile=.coveragerc"

black:
	docker-compose -f docker-compose.yml run --rm --service-ports api bash -c \
	"python -m black loans_api/"
