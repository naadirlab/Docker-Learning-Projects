FROM python:3.11-slim

WORKDIR /App

COPY . .

RUN pip install --no-cache-dir flask==3.1.2 redis==5.2.0

EXPOSE 5002

CMD ["python", "Flask_App.py"]