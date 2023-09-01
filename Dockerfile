# Use the official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    systemctl \
    nginx \
    python3-pip \
    python3-dev \
    python3-venv \
    gunicorn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for your Django project
RUN mkdir -p /app

# Change the working directory to /app
WORKDIR /app

# Clone your Django project from Git (replace with your Git repository URL)
RUN git clone https://github.com/Mutemi1998/myshop.git .

# Install Django project dependencies
RUN pip3 install -r requirements.txt
RUN pip install djangorestframework
RUN pip install markdown       
RUN pip install django-filter

# Expose port 80 for Nginx
EXPOSE 80

# Copy Nginx configuration file to the container
COPY config /etc/nginx/sites-available/config

RUN ln -s /etc/nginx/sites-available/config /etc/nginx/sites-enabled

RUN nginx -t

RUN systemctl restart nginx

# Collect static files and perform migrations
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate

# Start Gunicorn to serve your Django application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "myshop.wsgi:application"]
