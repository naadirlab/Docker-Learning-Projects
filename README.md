## Hello-Flask App

This project demonstrates how a simple Python Flask application is containerised using Docker.  
Later, the application is extended to run together with a MySQL database using Docker Compose.

---

### Python & Flask Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

### Dockerfile Steps
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

### Build Docker Image and Run Container

```bash
docker build -t hello-flask:latest .
docker run -d -p 5002:5002 hello-flask:latest
```

![alt text](<screenshots/Screenshot 2025-12-17 at 23.57.14.png>)

Screenshot showing the Flask app running successfully in a Docker container and accessible via the local browser on port 5002.


---

### Docker Compose (Running Multiple Containers)

Use **Docker Compose** to run the Hello-Flask App with a MySQL database. This creates a shared network for the containers. 

### docker-compose.yml

In this case, the application consists of:
- a **web service** (Flask app)
- a **database service** (MySQL)

```yaml
version: '3.8'

services:
  web:
    image: hello-flask:latest
    ports:
      - "5002:5002"
    depends_on:
      - mydb

  mydb:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
```

Key points briefly explained:
- services: lists all parts of the application
- image: specifies which Docker image to use
- ports: exposes the Flask app to the local machine
- depends_on: ensures the database starts before the web app

### Running the Application with Docker Compose

```bash
docker-compose up
```

---

### Result

A functional Flask application successfully running in a Docker container and locally accessible on port 5002. Using Docker Compose, the app connects automatically to the MySQL database, showing how multi-container apps can be managed easily and efficiently. 
