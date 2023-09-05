#!/bin/bash

# Start Gunicorn in the background
gunicorn -b 0.0.0.0:8000 myshop.wsgi:application &

# Start Nginx in the foreground
nginx -g "daemon off;"
