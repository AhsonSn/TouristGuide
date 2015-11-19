from flask import Blueprint, render_template

from app.basic.models import sidebar_items
from app.db.dbmanager import DBManager
from app.users.forms import LoginForm, RegisterForm

users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return 'Success'

    return render_template('login.html', login_form=login_form,
                           sidebar_items=sidebar_items)


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        db_manager = DBManager()

        if db_manager.insert_user(register_form):
            return render_template(
                'register.html', register_form=register_form,
                sidebar_items=sidebar_items, success=True,
                message='Sikeres regisztráció!')
        else:
            return render_template(
                'register.html', register_form=register_form,
                sidebar_items=sidebar_items, success=False,
                message='A felhasználónév vagy email már foglalt!')

    return render_template(
        'register.html', register_form=register_form,
        sidebar_items=sidebar_items, success=None, message='')
