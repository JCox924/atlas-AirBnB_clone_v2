#!/usr/bin/python3
"""
Starts a Flask web application that lists all State objects and their respective City objects from storage.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects and their respective City objects sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """
    Display a HTML page with a list of City objects linked to the State sorted by name.
    """
    state = storage.get(State, id)

    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
