from flask import Blueprint, render_template
from werkzeug.security import check_password_hash

from app.basic.models import sidebar_items
from app.db.dbmanager import DBManager
from app.users.forms import LoginForm, RegisterForm

users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = DBManager.get_user_by_name(login_form.name.data)
        if user is None:
            return 'Username not found'

        if check_password_hash(user.password, login_form.pwd.data):
            return 'Success'
        else:
            return 'Bad password'

    return render_template('login.html', login_form=login_form,
                           sidebar_items=sidebar_items)


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():

        if DBManager.insert_user(register_form):
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
