from flask import render_template, request, redirect
from facade import Facade, Event

facade = Facade()

def init_routes(app):
    @app.route('/')
    @app.route('/events')
    def index():
        events = facade.get_all_events()
        return render_template('index.html', events=events)

    @app.route('/discord')
    def discord():
        return render_template('discord.html')

    @app.route('/holbylon')
    def holbylon():
        return render_template('holbylon.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add_event():
        if request.method == 'POST':
            new_event = Event(
                name=request.form['name'],
                date=request.form['date'],
                location=request.form['location'],
                link=request.form['link']
            )
            facade.add_event(new_event)
            return redirect('/')
        return render_template('add_event.html')

    @app.route('/delete/<int:event_id>')
    def delete_event(event_id):
        facade.delete_event(event_id)
        return redirect('/')
