# myshop
e-comerce backend using django Redis and Rabbitmq running in docker containers

#run Rabbit mq in docker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

#Run celery worker 
celery -A myshop worker -l info
