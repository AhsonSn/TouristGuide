from flask import Flask
from flask_bootstrap import Bootstrap

from app.basic.views import basic
from app.users.views import users

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config')
app.register_blueprint(basic)
app.register_blueprint(users)
