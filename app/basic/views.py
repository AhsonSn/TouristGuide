from flask import Blueprint, render_template

basic = Blueprint('basic', __name__)


@basic.route('/')
def home():
    return render_template('home.html')
