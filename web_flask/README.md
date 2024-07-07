# Flask Web Application

This is a simple Flask web application with several routes that demonstrate basic functionality, including dynamic URL routing and HTML templating.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the Repository** (if applicable):
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
## Accessing the Routes
    Root route: http://0.0.0.0:5000/ - Displays “Hello HBNB!”

    /hbnb route: http://0.0.0.0:5000/hbnb - Displays “HBNB”
    
    /c/<text> route: http://0.0.0.0:5000/c/some_text - Displays “C some text” (replace some_text with any text, underscores _ will be replaced with spaces)

    /python/<text> route: http://0.0.0.0:5000/python/ - Displays “Python is cool”

    You can replace <text> with any text, e.g., http://0.0.0.0:5000/python/any_text - Displays “Python any text” (underscores _ will be replaced with spaces)

    /number/<n> route: http://0.0.0.0:5000/number/89 - Displays “89 is a number” (replace 89 with any integer)

    /number_template/<n> route: http://0.0.0.0:5000/number_template/89 - Displays an HTML page with “Number: 89” (replace 89 with any integer)