import flask

app = flask.Flask(__name__)
app.sidebar_items = [
    ('/login', 'login', 'Bejelentkezés'),
    ('/tours', 'tours', 'Túrák'),
    ('/statictics', 'statistics', 'Statisztikák')
]


@app.route('/')
def home():
    return flask.render_template('home.html', app=app)


@app.route('/login')
def login():
    return flask.render_template('login.html', app=app)


@app.route('/browser')
def browser():
    user_agent = flask.request.headers.get('User-Agent')
    return 'your browser is %s' % user_agent


if __name__ == '__main__':
    app.run()
