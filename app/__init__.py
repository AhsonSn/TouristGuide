from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
database = SQLAlchemy()
loginmanager = LoginManager()
loginmanager.login_view = "users.views.login"
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    bootstrap.init_app(app)
    database.init_app(app)
    loginmanager.init_app(app)
    mail.init_app(app)

    from .admin.views import admin as admin_blueprint
    from .basic.views import basic as basic_blueprint
    from .users.views import users as users_blueprint
    from .tours.views import tours_blueprint

    app.register_blueprint(basic_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(tours_blueprint)

    @app.template_filter('literal_date')
    def _jinja2_filter_literal_date(date):
        return date.strftime("%Y. %b. %d.")

    @app.template_filter('time')
    def _jinja2_filter_literal_date(date):
        return date.strftime("%H:%M")

    return app
