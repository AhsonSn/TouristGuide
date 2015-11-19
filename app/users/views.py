from flask import Blueprint, render_template
from html5print import HTMLBeautifier

from app.basic.models import sidebar_items
from app.users.forms import LoginForm, RegisterForm
from app.db.dbmanager import DBManager

users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return 'Success'

    return HTMLBeautifier.beautify(
        render_template('login.html', login_form=login_form,
                        sidebar_items=sidebar_items), 2)


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        db_manager = DBManager()
        succ = db_manager.insert_user(register_form)
        if succ:
            return HTMLBeautifier.beautify(
                render_template('register.html', register_form=register_form,
                                sidebar_items=sidebar_items, success=True, message=""),  2)
        else:
            return HTMLBeautifier.beautify(
                render_template('register.html', register_form=register_form,
                                sidebar_items=sidebar_items, success=False, message="A felhasználó név vagy email foglalt."),  2)

    return HTMLBeautifier.beautify(
        render_template('register.html', register_form=register_form,
                        sidebar_items=sidebar_items, success=False, message=""), 2)
