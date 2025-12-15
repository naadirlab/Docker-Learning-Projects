from flask import Flask
import redis 

app = Flask(__name__)

# Connect to the Redis database
redis_client = redis.Redis(
        host='redis',
        port=6379,
        decode_responses=True
    ) 

# First Route: Displays a welcome message
@app.route('/')
def welcome():
    return "Welcome to my Flask App!"
    
# Second Route: Displays the Visit Count
@app.route('/count')
def count():
    count = redis_client.incr('visitor_count')
    return f'This page has been visited: {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)