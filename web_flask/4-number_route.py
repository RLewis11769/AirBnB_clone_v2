#!/usr/bin/python3
"""
Starts Flask web application on 0.0.0.0 port 5000
Contains response for home page, /hbnb, and /c/<text>
Adds variable with default and second decorator compared to previous
"""

from flask import Flask, render_template


# Pass import_name/application package to Flask class
# Tells Flask where to find resources (ie templates, static files)
# Sets __name__ variable to module name (so depends on source file)
app = Flask(__name__)


# Determine which URL triggers function
# Meaning output of function rendered on home page in this instance
@app.route('/', strict_slashes=False)
def index():
    """ Displays 'Hello HBNB!' """
    # Return converted into response object with default parameters
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


@app.route('/c/<subpath>', strict_slashes=False)
def c_plus_anything(subpath):
    """ Displays C then text after /c/ """
    # subpath is variable denoted by app.route and passed in
    subpath = subpath.replace("_", " ")
    return "C %s" % subpath


@app.route('/python/', defaults={"subpath": "is cool"})
@app.route('/python/<subpath>', strict_slashes=False)
def python_plus_anything_default(subpath):
    """ Displays Python then text after /python/ with "is cool" default """
    # subpath is variable denoted by app.route and passed in
    subpath = subpath.replace("_", " ")
    return "Python %s" % subpath


@app.route('/number/<int:char>', strict_slashes=False)
def checkInt(char):
    """ Displays char is a number only if char is an int """
    # app.route only allows ints through, %d displays properly
    return "%d is a number" % char

# Calls function when called
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
