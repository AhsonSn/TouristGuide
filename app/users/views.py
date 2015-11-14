from flask import Blueprint, render_template

from app.basic.models import sidebar_items
from app.users.forms import LoginForm, RegisterForm

users = Blueprint('users', __name__)


@users.route('/login')
def login():
    nameform = LoginForm()
    return render_template('login.html', nameform=nameform, sidebar_items=sidebar_items)


@users.route('/register')
def register():
    register_form = RegisterForm()
    return render_template('register.html', register_form=register_form, sidebar_items=sidebar_items)
