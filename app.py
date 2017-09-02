
from flask import Flask
import redis

app = Flask(__name__)

r = redis.StrictRedis(host='redis', port=6379, db=0)
@app.route('/')
def hello_world():
    r.incr("count")
    n = r.get("count").decode("utf-8")
    return f"Hello world!!\nあなたは{n}回目の訪問者です"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

