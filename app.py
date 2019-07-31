from os import environ

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f'Hello {environ.get("ARG_EX", "World")}!'

