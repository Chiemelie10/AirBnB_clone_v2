#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name__)
"""Craetes an instance of flask."""


@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB! on the home page"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB on the hbnb page"""

    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
