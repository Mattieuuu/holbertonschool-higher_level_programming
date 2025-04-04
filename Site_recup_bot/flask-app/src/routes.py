from flask import render_template
from facade import Facade

facade = Facade()

def init_routes(app):
    @app.route('/')
    def index():
        events = facade.get_all_events()
        return render_template('index.html', events=events)

    @app.route('/add', methods=['GET', 'POST'])
    def add_event():
        return render_template('add_event.html')
