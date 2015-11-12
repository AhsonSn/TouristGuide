from flask import Flask

from app.basic.views import basic

app = Flask(__name__)
app.register_blueprint(basic)
