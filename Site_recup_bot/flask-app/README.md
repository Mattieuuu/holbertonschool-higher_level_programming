# README.md

# Flask Application

This is a simple Flask application that demonstrates the basic structure and functionality of a web application using Flask.

## Project Structure

```
flask-app
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── routes
│   │   └── __init__.py       # Defines the routes for the application
│   ├── templates
│   │   └── index.html        # Main HTML template for the application
│   └── static
│       └── style.css         # CSS styles for the application
├── tests
│   └── __init__.py           # Organizes the test suite for the application
├── requirements.txt           # Lists the dependencies required for the project
└── README.md                  # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python src/app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Running Tests

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.