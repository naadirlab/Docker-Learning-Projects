# Hello-Flask App

## What is Flask?
Flask is a simple and lightweight framework for creating web applications in Python.

---

## Python & Flask Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

## Dockerfile Steps
A Dockerfile is a text file that contains a series of instructions on how to build a container image for an application.

1. Create Dockerfile

```bash
touch Dockerfile
```

2.	Set base image

```dockerfile
FROM python:3.8-bullseye
WORKDIR /app
COPY . .
```

3.	Install system dependencies

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev default-libmysqlclient-dev pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
```

4.	Install Python dependencies

```dockerfile
RUN pip install --no-cache-dir flask mysqlclient
```

5. Expose port 

```dockerfile
EXPOSE 5002
```

6. Run App
```dockerfile
CMD ["python", "app.py"]
```

## Build & Run Docker Container

```bash
docker build -t hello-flask .
docker run -d -p 5002:5002 hello-flask
docker ps
```
**Why `-p 5002:5002`?**
This maps port 5002 on your host machine to port 5002 inside the container.

## Summary

I containerised my Python web app using Docker, installed the necessary system and Python dependencies, built the Docker image, and ran it locally, making the app accessible via port 5002.