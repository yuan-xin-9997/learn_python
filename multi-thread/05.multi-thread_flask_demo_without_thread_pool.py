import flask
import time
import json

app = flask.Flask(__name__)


def read_file():
    time.sleep(0.1)
    return "read_file"

def read_db():
    time.sleep(0.2)
    return "read_db"

def read_api():
    time.sleep(0.3)
    return "read_api"

@app.route("/")
def index():
    result_file = read_file()
    result_db = read_db()
    result_api = read_api()

    return json.dumps(
        {
           "result_file": result_file,
           "result_db": result_db,
           "result_api": result_api 
        }
    )

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001
    )
    