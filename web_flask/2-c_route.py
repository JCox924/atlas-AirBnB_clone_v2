#!/usr/bin/python3

'''
Starts Flask web app with Flask routes

'''
from flask import Flask

app = Flask(__name__)

#home route
@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'
#route to /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'
#route to formatted text
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)