#!/bin/bash -e

if [[ "${1}" == "dev" ]]; then
    waitforit -host=db -port=5432 --timeout 30
    python manage.py createcachetable
    python manage.py migrate --no-input
    python manage.py runserver 0.0.0.0:9000
elif [[ "${1}" == "dist" ]]; then
    python /code/manage.py collectstatic --noinput
    python manage.py createcachetable
    python /code/manage.py migrate --no-input
    gunicorn wsgi -c gunicorn.py
else
    echo "Unknown command: ${1}"
    exit 1
fi
