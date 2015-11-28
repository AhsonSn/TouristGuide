from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm
from ..basic.models import sidebar_items
from ..db.dbfactory import DBFactory
from ..db.experiencemanager import ExperienceManager


users = Blueprint('users', __name__)


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        instance = DBFactory.get_instance()
        user = instance.User.get_user_by_name(login_form)

        if not user:
            return render_template('login.html', login_form=login_form,
                                   sidebar_items=sidebar_items, error=True)

        remember_me = login_form.remember_me.data

        login_user(user, remember_me)

        return redirect(url_for('tours.tours'))

    return render_template('login.html', login_form=login_form,
                           sidebar_items=sidebar_items, error=False)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('basic.home'))


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()
    register_form.experience.choices = [(e.id, e.name) for e in ExperienceManager.get_experiences()]

    if register_form.validate_on_submit():
        instance = DBFactory.get_instance()
        if instance.User.insert_user(register_form, register_form.experience.data):
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
