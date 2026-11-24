import os
import redis
from flask import Flask, app, jsonify

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, decode_responses=True)


@app.route('/')

def home():
    hits = cache.incr('hits')
    return jsonify({"message": "Hello from docker!", "hits": hits})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})