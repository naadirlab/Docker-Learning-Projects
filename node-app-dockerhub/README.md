# Node-App

This project demonstrates a simple Node.js application using Express.
It shows how to containerise a Node app with Docker, and optimise the image using multi-stage builds and a lightweight base image. Finally, this project shows how to push your images to DockerHub.

## Node & Express Setup

Install Node.js (macOS):

```bash
brew install node
```

Create package.json and install Express

```bash
npm init -y          # Creates package.json with default settings
npm install express  # Installs Express framework
```

## App Overview
The app.js file contains a simple Express app with one route:
- / : Returns a welcome message.

```javascript
// app.js
const express = require('express');
const app = express();
const port = 5002;

// Route
app.get('/', (req, res) => {
  res.send('Welcome to my Node App!');
});

// Start server
app.listen(port, '0.0.0.0', () => {
  console.log(`Node app listening at http://0.0.0.0:${port}`);
});
```

The server listens on 0.0.0.0 so that it can be accessed from the host machine or other containers.

## Dockerfile (Heavy Image)

**Note:** When I first built this image, I noticed it was very heavy. This is why I'd recommend to go to the next step, where I explained the steps by using a lightweight base image and multi-stage builds, making the image much lighter.  

```dockerfile
FROM node:24

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5002

CMD ["node", "app.js"]
```

## Dockerfile (Multi-stage Build) -> Lightweight Image

```dockerfile
# Stage 1: Build
FROM node:24-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm install

# Stage 2: Production
FROM node:24-slim
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY . .

EXPOSE 5002
CMD ["node", "app.js"]
```

Why Multi-stage Builds?
- The initial image including all build tools can be very large. 
- Multi-stage builds copy only the final app and runtime dependencies, creating a lighter image.
- This reduces storage and speeds up deployments.

## Build and Run Docker Image

Build the image

```bash
docker build -t node-app:v1 .
```

Run the container 

```bash
docker run -d -p 5002:5002 node-app:v1
```

The app should be accessible locally at http://127.0.0.1:5002

![alt text](../screenshots/Welcome_Page_Node.png)

## From 1.63GB to 353MB
**This highlights the significance of optimizing Docker images.**
By Reducing the image size, we removed unnecessary build tools and dependencies, making the image more lightweigt. 

![alt text](../screenshots/Reduce_Disk_Usage.png)

## Create a DockerHub Repository 

What is DockerHub?
DockerHub is a public registry for storing, sharing, and accessing Docker images.
It allows developers to pull images and push their own.

DockerHub -> Repositories -> Create A Repository

![alt text](../screenshots/DockerHub_Repo.png)

## Push Image to DockerHub

Tag the image for DockerHub:

```bash
docker tag node-app:v1 nashardocker/node-app:v1
```

Push the image:

```bash
docker push nashardocker/node-app:v1
```

Pushed Image:

![alt text](../screenshots/Pushed_Image_DockerHub.png)

## Result
A simple Node.js application running in a Docker container, accessible locally at http://127.0.0.1:5002.
The image is pushed to DockerHub and optimized using multi-stage builds, which makes it smaller and more efficient for deployment.