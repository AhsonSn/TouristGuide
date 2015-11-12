from flask import Blueprint, render_template, request

from app.basic.models import sidebar_items

basic = Blueprint('basic', __name__)


@basic.route('/')
def home():
    return render_template('home.html', sidebar_items=sidebar_items)


@basic.route('/login')
def login():
    return render_template('login.html', sidebar_items=sidebar_items)


@basic.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return 'your browser is %s' % user_agent
