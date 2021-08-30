#!/bin/sh
sleep 20
python manage.py makemigrations 

python manage.py migrate 

#python manage.py migrate --no-input
python manage.py collectstatic
#python manage.py runserver 0.0.0.0:8000
gunicorn wsgi:application --bind 0.0.0.0:8000

