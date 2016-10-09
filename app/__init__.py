from flask import Flask

app = Flask(__name__)


@app.route(r'/hello')
def hello():
    return "<p>hello</p>"

