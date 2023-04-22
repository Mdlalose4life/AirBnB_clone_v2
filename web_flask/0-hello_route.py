#!/usr/bin/python3
# script that starts a Web application

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
