# Instructions

Download [Docker Desktop](https://docs.docker.com/get-docker/)

*Make sure you're in with ```$ docker login```*

From the command line, download the Docker image for Redis:

```$ docker pull redis```

You can check to see if the image was successfully pulled from Docker with this:

```$ docker image ls```

Now, run a container with the Redis image. 
Because we're using the JSON extension of Redis, the container would be run with the 'redis/redis-stack-server' image instead of the usual 'redis' image

```$ docker run -d --name some-redis --rm -p 6379:6379 redis/redis-stack-server```

Check to see if the container was created:

```$ docker container ls``` 

or 

```$ docker ps```

Connect to the container as well as the Redis CLI:

```$ docker exec -it some-redis redis-cli```

You can run Redis commands through here to view the content of the database in another way

**Make sure to stop the container if you're not using it anymore to avoid ghost servers 👻**
