#!/usr/bin/env bash
echo migration start
python manage.py migrate
echo migration end
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8080