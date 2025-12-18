# Stage 1: Build Stage
FROM python:3.8-bullseye as Build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir flask mysqlclient

# Stage 2: Production Stage
FROM python:3.8-bullseye

WORKDIR /app

COPY --from=Build /app /app

EXPOSE 5002

CMD ["python", "app.py"]