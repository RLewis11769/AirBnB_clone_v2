#!/usr/bin/python3
"""
Starts Flask web application on 0.0.0.0 port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State


# application context is created before new request and closes when finished
@app.teardown_appcontext
def teardown():
    """ Removes current Session so can can create new one """
    storage.close()

@app.route('/', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', value=models.storage.all(State).values())
