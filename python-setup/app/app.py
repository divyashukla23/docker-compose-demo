from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (service name = redis)
r = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    count = r.incr('visits')
    return f"Hello! You have visited {count} times 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)