#!/usr/bin/python3
"""Starting the Flask App"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=True)
def states_list():
    """Render the states list"""
    states = storage.all("States")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Closes the database connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
