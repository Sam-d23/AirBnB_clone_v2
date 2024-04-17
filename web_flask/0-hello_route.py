#!/usr/bin/env python3
"""
Script starting a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    #The Flask development server is started
    #Listens on all network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

