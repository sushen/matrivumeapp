from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is my matrivume and I want smooth piplie angagement ok"


if __name__ == "__main__":
    app.run()
