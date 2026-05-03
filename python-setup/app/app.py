# from flask import Flask
# import redis

# app = Flask(__name__)

# # Connect to Redis (service name = redis)
# r = redis.Redis(host='redis', port=6379)

# @app.route("/")
# def home():
#     count = r.incr('visits')
#     return f"Hello! You have visited {count} times 🚀"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask
import psycopg2
import time

app = Flask(__name__)

# Retry logic (VERY IMPORTANT)
for i in range(5):
    try:
        conn = psycopg2.connect(
            host="db",
            database="testdb",
            user="user",
            password="password"
        )
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY
            )
        """)
        conn.commit()
        break
    except Exception as e:
        print("DB not ready, retrying...")
        time.sleep(2)

@app.route("/")
def home():
    cursor.execute("INSERT INTO visits DEFAULT VALUES")
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]

    return f"Hello! Total records: {count} 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)