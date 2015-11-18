from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app.basic.views import basic
from app.users.views import users

tourist_guide = Flask(__name__)
tourist_guide.config.from_object('config')

bootstrap = Bootstrap(tourist_guide)
database = SQLAlchemy(tourist_guide)

tourist_guide.register_blueprint(basic)
tourist_guide.register_blueprint(users)
