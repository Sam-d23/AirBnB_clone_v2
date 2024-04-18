#!/usr/bin/env python3
"""
Configured to serve its content from the route /airbnb-onepage/ on port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/")
def hello_hbnb():
    """Route that displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
