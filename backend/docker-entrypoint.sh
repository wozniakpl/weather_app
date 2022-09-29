#!/bin/bash -e

waitforit -host=db -port=5432 --timeout 30
python manage.py createcachetable
python manage.py migrate
python manage.py runserver 0.0.0.0:9000
