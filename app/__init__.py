from flask import Flask

from app.basic.views import basic
from app.users.views import users

app = Flask(__name__)
app.register_blueprint(basic)
app.register_blueprint(users)
