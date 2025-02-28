# Flask Unit Testing

## Overview
This project demonstrates how to write unit tests for a Flask application using `unittest` and `pytest`. The repository contains a simple Flask app and test cases to ensure its functionality.

## Features
- Flask app with basic routes
- Unit testing using `unittest` and `pytest`
- Test coverage for different scenarios

## Requirements
Ensure you have the following installed:
- Python 3.7+
- Flask
- pytest
- unittest

You can install the dependencies using:
```sh
pip install -r requirements.txt
```

## Project Structure
```
flask-unit-test-1/
│-- app.py        # Main Flask application
│-- test_app.py   # Unit tests for Flask app
│-- requirements.txt  # Dependencies
│-- README.md     # Project documentation
```

## Running the Flask App
To start the Flask application, run:
```sh
python app.py
```

## Running Unit Tests
You can run the unit tests using `unittest`:
```sh
python -m unittest discover
```
Or using `pytest`:
```sh
pytest
```

## Contributing
Feel free to fork this repository and submit pull requests to improve the unit tests.

## License
This project is licensed under the MIT License.

