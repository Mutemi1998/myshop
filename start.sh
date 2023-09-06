#!/bin/bash

#make migrations 
python3 manage.py migrate &

#create superuser
python3 manage.py createsuperuser --noinput &

# Start Gunicorn in the background
gunicorn -b 0.0.0.0:8000 myshop.wsgi:application --access-logfile /var/log/gunicorn/access.log  --error-logfile /var/log/gunicorn/error.log  &

# Start Nginx in the foreground
nginx -g "daemon off;"
