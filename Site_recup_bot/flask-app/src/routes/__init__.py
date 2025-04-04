from flask import Blueprint

# Create a blueprint for the routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the Flask App!"