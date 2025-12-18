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