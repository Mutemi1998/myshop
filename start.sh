#!/bin/bash

# Define the MySQL container name
MYSQL_CONTAINER_NAME="mysql-container"

# Wait until mysql-container is up and running
while true; do
    # Try to ping the MySQL container
    if ping -q -c 1 -w 1 ${MYSQL_CONTAINER_NAME} >/dev/null; then
        echo "mysql-container is up and running."
        #give mysql service time to start
        sleep 10
        break
    else
        echo "Waiting for mysql-container to start..."
        sleep 5  # Adjust the sleep interval as needed
    fi
done

# Run migrations
python3 manage.py migrate


# Run migrations
python3 manage.py migrate

#create superuser
python3 manage.py createsuperuser --noinput &

# Start Gunicorn in the background
gunicorn -b 0.0.0.0:8000 myshop.wsgi:application --access-logfile /var/log/gunicorn/access.log  --error-logfile /var/log/gunicorn/error.log  &

# Start Nginx in the foreground
nginx -g "daemon off;"
