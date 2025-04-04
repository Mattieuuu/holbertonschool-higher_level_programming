from flask import Flask
from routes_config import init_routes  # Changed import name to avoid conflict
from facade import Facade

app = Flask(__name__)
facade = Facade()

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)