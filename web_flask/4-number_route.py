#!/usr/bin/python3
"""
script that starts a Web application
"""


from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route("/", strict_slashes=False)
def hello():
    """ returns Hello HBNB """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ returns HBNB """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    Displays C then
    Retuns the given string, and replaces underscores with
    a space
    """
    string = "C {}".format(text.replace("_", " "))
    return string


@app.route("/python")
@app.route("/python/<text>",strict_slashes=False)
def python(text="is_cool"):
    """
    Displays Python then returns the given text then
    replaces underscores with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """
    Displays the n if n is an integer
    """
    return "{} is a number".format(int(n))


if __name__ == "__main__":
    app.run()
