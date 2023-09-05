#!/bin/bash

# Start Gunicorn in the background
gunicorn -b 0.0.0.0:8000 myshop.wsgi:application --access-logfile /var/log/gunicorn/access.log  --error-logfile /var/log/gunicorn/error.log  &

# Start Nginx in the foreground
nginx -g "daemon off;"
