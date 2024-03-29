#!/usr/bin/python3
"""
Module that starts a flask app
listening to 0.0.0.0:5000
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """A HTML page with a list of all State objects in DBStorage is dispalyed,
    with States sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """The current SQLAlchemy session is removed."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
