#!/bin/bash -e

if [[ "${1}" == "dev" ]]; then
    waitforit -host=db -port=5432 --timeout 30
    python manage.py createcachetable
    python manage.py migrate
    python manage.py runserver 0.0.0.0:9000
elif [[ "${1}" == "dist" ]]; then
    echo "TODO"
else
    echo "Unknown command: ${1}"
    exit 1
fi
