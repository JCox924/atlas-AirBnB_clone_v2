#!/usr/bin/python3

'''
Starts Flask web app with Flask routes
'''

from flask import Flask, render_template

app = Flask(__name__)

#home route
@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'
#route to /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    app.logger.info('HBNB')
    return 'HBNB'
#route to /c/formatted text
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    app.logger.info(f'text: {text}')
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"
#route to /python/formatted text

@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    app.logger.info(f'text: {text}')
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    app.logger.info(f'Number {n}')
    return f"{n} is a number"
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)