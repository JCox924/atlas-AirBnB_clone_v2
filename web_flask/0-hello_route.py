#!/usr/bin/python3

'''
Starts Flask web app with Flask routes
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Route that returns 'Hello HBNB!'"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)