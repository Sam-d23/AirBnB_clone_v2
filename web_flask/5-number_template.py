#!/usr/bin/python3
"""
Script that starts a Flask web application with six routes.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route displaying 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route displaying 'HBNB'."""
    return 'HBNB'


@app.route('/c/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Route displaying 'C' followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """Route displaying 'Python' followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Route displaying 'n is a number' if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Route displaying an HTML page with number n."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
