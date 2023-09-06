# Myshop
e-comerce backend using django Redis and Rabbitmq running in docker containers

# Run Rabbit mq in docker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

# Run celery worker 
celery -A myshop worker -l info

# Running the E-commerce site
clone the repository

Then  change pwd to myshop


docker-compose up --build -d

Then check http://<ip>


# Set Super admin credentials in docker file