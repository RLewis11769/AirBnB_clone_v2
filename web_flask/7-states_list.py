#!/usr/bin/python3
"""
Starts Flask web application on 0.0.0.0 port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


# application context is created before new request and closes when finished
@app.teardown_appcontext
def teardown(self):
    """ Removes current Session so can can create new one """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Prints list of State values to html """
    # Creates list of all values in State storage
    values = storage.all(State).values()
    # Sorts list by state.name basically
    # sorted requires key, lambda doesn't need name bc diff for db vs file
    states = sorted(values, key=lambda x: x.name)
    # Passes sorted list to html file which loops over
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
