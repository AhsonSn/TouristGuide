from flask import Blueprint, render_template
from html5print import HTMLBeautifier

from app.basic.models import sidebar_items
from app.users.forms import LoginForm, RegisterForm

users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return 'Success'

    return HTMLBeautifier.beautify(render_template('login.html', login_form=login_form, sidebar_items=sidebar_items), 2)


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        return 'Success'

    return HTMLBeautifier.beautify(
        render_template('register.html', register_form=register_form, sidebar_items=sidebar_items), 2)
