# Use more stable Python image
FROM python:3.8-bullseye

WORKDIR /app

COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir flask mysqlclient

EXPOSE 5002

CMD ["python", "app.py"]