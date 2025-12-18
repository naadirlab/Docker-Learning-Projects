# Flask-Redis App
This project shows step by step how to use Redis to store and retrieve data.
It demonstrates a multi-container setup with Docker Compose, including a Flask web app, a Redis database, and a Nginx load balancer for handling multiple app instances.

## App Overview

The Flask_App.py file contains a Flask application with two routes:
- / : Displays a welcome message in large text, centered on the page.
- /count : Displays a visitor count stored in Redis.

```python
from flask import Flask
import redis

app = Flask(__name__)

# Connects to Redis database
redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

# First Route
@app.route('/')
def welcome():
    return "Welcome to my Flask App!"

# Second Route
@app.route('/count')
def count():
    count = redis_client.incr('visitor_count')
    return f"📊 This page has been visited: {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
```

The line `if __name__ == '__main__': app.run(host='0.0.0.0', port=5002)` starts the Flask server.  
Using `host='0.0.0.0'` ensures that the server listens on all network interfaces, which is important so that other containers (like Redis) or the host machine can access the app.

## Dockerfile

Note: Using a python:3.11-slim base image gives a lightweight Python environment.
It contains only the essential components, making the Docker image smaller and faster to build.

```dockerfile
FROM python:3.11-slim
WORKDIR /App
COPY . .
RUN pip install --no-cache-dir flask==3.1.2 redis==5.2.0
EXPOSE 5002
CMD ["python", "Flask_App.py"]
```

## Docker Compose

The application is run together with a Redis database, creating a shared network for the containers.
- services: define the different parts of the application (web, redis, nginx).
- volumes: allow data to persist even if a container stops or is removed (here redis-data stores Redis data).

```yaml
version: '3.11'

services:
  web:
    build: .
    expose:
      - "5002"
    depends_on:
      - redis

  redis:
    image: "redis:latest"
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

  nginx:
    image: nginx:latest
    ports:
      - "5002:5002"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  redis-data:
```

## nginx.conf file 

``` 
events {}

http {
    upstream flask_app {
        server web:5002;
    }

    server {
        listen 5002;

        location / {
            proxy_pass http://flask_app;
        }
    }
}
``` 

Why use Nginx here?
- When scaling the Flask app to multiple containers, you can’t bind all instances to the same host port.
- Nginx acts as a reverse proxy / load balancer, distributing incoming requests across multiple Flask containers.
- This setup makes the application capable to handle higher traffic.


## Run Docker-Compose

```bash
docker-compose up
```

When the command is run, the application should be accessible locally at http://127.0.0.1:5002.

## Result

A fully functional Flask application that keeps track of visitor counts, connected to a Redis database, all running in Docker containers.

![alt text](../screenshots/Results.png)