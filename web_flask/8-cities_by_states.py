#!/usr/bin/python3
"""
Starts a Flask web application that lists all State objects and their respective City objects from storage.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects and their respective City objects sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)