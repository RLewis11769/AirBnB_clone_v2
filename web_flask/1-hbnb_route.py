#!/usr/bin/python3
"""
Starts Flask web application on 0.0.0.0 port 5000
Contains response for 2 URLS
"""

from flask import Flask


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

# Calls function when called
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
