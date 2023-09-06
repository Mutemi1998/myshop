# Use the official Ubuntu as a parent image
FROM ubuntu

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

RUN apt update
# Update and install necessary packages
RUN apt install -y \
    git \
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
RUN pip3 install -r requirements.txt \
    && pip install djangorestframework \
    && pip install markdown \
    && pip install django-filter
# Expose port 80 for Nginx
EXPOSE 80


# Copy Nginx configuration file to the container
RUN rm /etc/nginx/sites-enabled/default 
RUN rm /etc/nginx/sites-available/default

COPY config /etc/nginx/sites-available/config

RUN ln -s /etc/nginx/sites-available/config /etc/nginx/sites-enabled

RUN nginx -t

# Collect static files and perform migrations
RUN python3 manage.py collectstatic --noinput 

# Copy the start script into the container
COPY start.sh /start.sh

#Set credentials for superuser
ENV DJANGO_SUPERUSER_USERNAME=commerce
ENV DJANGO_SUPERUSER_EMAIL=commerce@commerce.com
ENV DJANGO_SUPERUSER_PASSWORD=password


# Make the script executable
RUN chmod +x /start.sh

# Set the script as the CMD
CMD ["/start.sh"]