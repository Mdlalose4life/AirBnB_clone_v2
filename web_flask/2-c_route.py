#!/usr/bin/python3
"""
script that starts a Web application
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ returns Hello HBNB """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ returns HBNB """
    return 'HBNB'


@app.route("/c/<text>")
def text(text):
    """
    Retuns the given string, and replaces underscores with
    a space
    """
    string = "C {}".format(text.replace("_", " "))
    return string


if __name__ == '__main__':
    app.run()
