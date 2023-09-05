# Myshop
e-comerce backend using django Redis and Rabbitmq running in docker containers

# Run Rabbit mq in docker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

# Run celery worker 
celery -A myshop worker -l info

# Running the E-commerce site
clone the repository

Then  change pwd to myshop

# Build docker image

docker build -t  myshop .

# Run the image

 docker run -d -p 80:80 myshop
