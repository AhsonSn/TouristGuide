from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
database = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    bootstrap.init_app(app)
    database.init_app(app)

    from .admin.views import admin as admin_blueprint
    from .basic.views import basic as basic_blueprint
    from .users.views import users as users_blueprint
    from .toursupervisor.views import toursupervisor as toursupervisor_blueprint

    app.register_blueprint(basic_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(toursupervisor_blueprint)

    return app
