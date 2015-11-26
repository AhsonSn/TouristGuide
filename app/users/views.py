from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm
from ..basic.models import sidebar_items
from ..db.dbfactory import DBFactory

users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        instance = DBFactory.get_instance()
        user = instance.User.get_user_by_name(login_form)
        remember_me = login_form.remember_me.data

        if login_user(user, remember_me):
            flash('Logged in successfully.')
        else:
            flash('Unable to log in.')

        return redirect(url_for('basic.home'))

    return render_template('login.html', login_form=login_form,
                           sidebar_items=sidebar_items)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('basic.home'))


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        instance = DBFactory.get_instance()
        if instance.User.insert_user(register_form):
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
