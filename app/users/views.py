from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from .forms import LoginForm, RegisterForm, SettingsForm, MessageForm
from ..db.experiencemanager import ExperienceDAO
from ..db.messagemanager import MessageDAO
from ..db.notificationmanager import NotificationDAO
from ..db.registrationmanager import RegistrationDAO
from ..db.tourmanager import TourDAO
from ..db.usermanager import UserDAO

users = Blueprint('users', __name__)


@users.route('/create')
def create_table():
    from app import database
    database.create_all()    
    return redirect(url_for('basic.home'))


@users.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = UserDAO.get_user_by_name(login_form)

        if not user:
            return render_template('login.html', login_form=login_form,
                                   error=True,
                                   message='Nincs ilyen felhasználó!')

        if not check_password_hash(user.password, login_form.pwd.data):
            return render_template('login.html', login_form=login_form,
                                   error=True,
                                   message='Rossz jelszó!')

        remember_me = login_form.remember_me.data

        login_user(user, remember_me)

        return redirect(url_for('tours.tours_default'))

    return render_template('login.html', login_form=login_form,
                           error=False,
                           message=None)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('basic.home'))


@users.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()
    register_form.experience.choices = [(e.id, e.name) for e in
                                        ExperienceDAO.get_experiences()]

    if register_form.validate_on_submit():
        if UserDAO.insert_user(register_form,
                               register_form.experience.data):
            return render_template(
                    'register.html', register_form=register_form,
                    success=True,
                    message='Sikeres regisztráció!')
        else:
            return render_template(
                    'register.html', register_form=register_form,
                    success=False,
                    message='A felhasználónév vagy email már foglalt!')

    return render_template(
            'register.html', register_form=register_form,
            success=None, message='')


@users.route('/settings', methods=('GET', 'POST'))
@login_required
def settings():
    settings_form = SettingsForm()
    settings_form.experience.choices = [(e.id, e.name) for e in
                                        ExperienceDAO.get_experiences()]

    if settings_form.validate_on_submit():
        if not check_password_hash(current_user.password,
                                   settings_form.old_pwd.data):
            return render_template(
                    'settings.html', settings_form=settings_form,
                    experience=current_user.experience_id,
                    success=False, message='Rossz jelszó!')

        if settings_form.name.data != current_user.username:
            UserDAO.update_username(current_user.id,
                                    settings_form.name.data)

        if settings_form.new_pwd.data:
            UserDAO.update_pwd(current_user.username,
                               settings_form.new_pwd.data)

        if settings_form.email.data != current_user.email:
            UserDAO.update_email(current_user.username,
                                 settings_form.email.data)

        UserDAO.update_experience(current_user.username,
                                  settings_form.experience.data)

        if settings_form.phoneNumber.data != current_user.phone:
            UserDAO.update_phone(current_user.username,
                                 settings_form.phoneNumber.data)

        if settings_form.avatar.has_file():
            UserDAO.update_avatar(current_user.username,
                                  request.files['avatar'])

        return render_template(
                'settings.html', settings_form=settings_form,
                experience=current_user.experience_id,
                success=True, message='A beállításaidat elmentettük.')

    settings_form.name.data = current_user.username
    settings_form.email.data = current_user.email
    settings_form.experience.data = current_user.experience
    settings_form.phoneNumber.data = current_user.phone

    return render_template(
            'settings.html', settings_form=settings_form,
            experience=current_user.experience_id,
            success=None, message='')


@users.route('/apply-for-tour/<int:tour_id>')
@login_required
def apply_for_tour(tour_id):
    tour = TourDAO.get_tour_by_id(tour_id)
    success = RegistrationDAO.register_user(current_user, tour)
    if success[0] == 0:
        current_user.allowance = UserDAO.incTour(current_user)

    return render_template(
            'apply.html', tour=tour, success=success[0], tourname=success[1])


@users.route('/detach-from-tour/<int:tour_id>')
@login_required
def detach_from_tour(tour_id):
    tour = TourDAO.get_tour_by_id(tour_id)
    success = RegistrationDAO.unregister_user(current_user.id, tour)
    if success:
        UserDAO.decTour(current_user)

    return render_template(
            'detach.html', tour=tour, success=success)


@users.route('/registrations')
@login_required
def registrations():
    regs = RegistrationDAO.get_registrations_of_user(current_user)
    results = []

    for reg in regs:
        results.append(TourDAO.get_tour_by_id(reg.tour_id))

    return render_template(
            'registrations.html', results=results,
            user=current_user)


@users.route('/username-available/<username>')
@login_required
def username_available(username):
    return '0' if UserDAO.get_user_with_name(username) else '1'


@users.route('/messages')
@login_required
def messages():
    if current_user.account_type_id != 1:
        return redirect('/')

    mess = MessageDAO.get_list()

    return render_template('message.html', results=mess)


@users.route('/writemessages', methods=('GET', 'POST'))
@login_required
def writemessages():
    if current_user.account_type_id != 2:
        return redirect('/')

    message_form = MessageForm()

    if message_form.validate_on_submit():
        MessageDAO.insert_new_message(current_user.id,
                                      message_form.subject.data,
                                      message_form.message.data)

        return render_template('writemessage.html',
                               message_form=message_form,
                               message='Az üzenetet sikeresen elküldtük!')

    return render_template('writemessage.html',
                           message_form=message_form, message='')


@users.route('/checkmail')
@login_required
def checkmail():
    return str(MessageDAO.get_new_mails_count())


@users.route('/readmail/<messageid>')
@login_required
def readmail(messageid):
    success = MessageDAO.refreshRead(messageid, 1)

    return '0'


@users.route('/deletemessage/<mid>')
@login_required
def deletemessage(mid):
    MessageDAO.delete(mid)

    return redirect("/messages")

@users.route('/checknotification')
@login_required
def checknotification():
    return str(NotificationDAO.get_new_mails_count(current_user))

@users.route('/notification')
@login_required
def notification():
    if current_user.account_type_id != 3:
        return redirect('/')

    mess = NotificationDAO.get_list(current_user)

    return render_template('message.html', results=mess)
