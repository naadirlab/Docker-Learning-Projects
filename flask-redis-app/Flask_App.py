from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

@app.route('/')
def welcome():
    return """
    <html>
      <head>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 40px;
            font-family: Arial, sans-serif;
            text-align: center;
          }
        </style>
      </head>
      <body>
        Welcome to my Flask App!
      </body>
    </html>
    """

@app.route('/count')
def count():
    count = redis_client.incr('visitor_count')
    return f"""
    <html>
      <head>
        <style>
          body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 40px;
            font-family: Arial, sans-serif;
            text-align: center;
          }}
        </style>
      </head>
      <body>
        📊 This page has been visited: {count} times.
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)