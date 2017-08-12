
from flask import Flask

app = Flask(__name__)

n = 0
@app.route('/')
def hello_world():
    global n
    n += 1
    return f"Hello world!!\nあなたは{n}回目の訪問者です"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

