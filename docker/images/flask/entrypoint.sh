#!/bin/bash
until nc -z ${DB_HOST} 3306; do
    sleep 1
done

flask db upgrade

exec gunicorn --config gunicorn_config.py wsgi:app
