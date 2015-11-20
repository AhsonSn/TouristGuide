from werkzeug.security import generate_password_hash
from app import database
from .models import User, Experience, Role, Tour
from datetime import datetime


class DBManager(object):
    @staticmethod
    def insert_user(form):
        """
        Inserts a user to database, from the registration form.

        Password will not be stored in Database, only password sha1s.
        This method checks if a username or email is already in the database.
        If it does, this method returns False.
        If it doesn't, then adds a new user to the database.
        :param form: a form which contains a name, email, pwd
        :return: True if success, False otherwise
        """
        passw = generate_password_hash(form.pwd.data)
        n = form.name.data
        e = form.email.data
        user = User(n, passw, e)
        user.account_type_id = 3
        user.experience_id = 1
        user.fullname = ""

        if DBManager.get_user_by_name(n) is not None \
                or DBManager.get_user_by_email(e) is not None:
            return False

        database.session.add(user)
        database.session.commit()
        return True

    @staticmethod
    def get_user_by_name(name):
        """
        Return a User instance where username is equal name.
        :param name: username
        :return: User instance
        """
        return User.query.filter_by(username=name).first()

    @staticmethod
    def get_user_by_email(email_):
        """
        Return a User instance where email is equal email.
        :param email_: Users emails
        :return: User instance
        """
        return User.query.filter_by(email=email_).first()

    @staticmethod
    def get_experiences():
        """
        Return a list of Experience from database.
        :return: list of Experience
        """
        return Experience.query.all()

    @staticmethod
    def get_user_by_role(role_name):
        """
        Return a list of user, who's account type is role_name.
        :param role_name: Account_type_name
        :return: list of specified user
        """
        role = Role.query.filter_by(name=role_name).first()
        if role is not None:
            users = User.query.filter_by(account_type_id=role.id).all()
            if users is not None:
                return users

        return None

    @staticmethod
    def insert_tour(name, start_date, end_date, exp_id, tg_id, description, images="", dateformat="%Y-%m-%d %H:%M"):
        """
        Insert a new tour to database. The default date format is yyyy.mm.dd hh:mi, so date is a string. If you want to
        change date format, give the dateformat parameter.
        :param name: Tour name
        :param start_date: string of start date time of tour
        :param end_date: string of end date time of tour
        :param exp_id: experience id
        :param tg_id: tour guide id
        :param description: description of tour
        :param images: (Optional) tour images src
        :param dateformat: (Optional) a format string to start and end date.
        :return:
        """

        tour = Tour(name, exp_id, tg_id)
        tour.start_datetime = datetime.strptime(start_date, dateformat)
        tour.end_datetime = datetime.strptime(end_date, dateformat)
        tour.images = images
        tour.description = description
        database.session.add(tour)
        database.session.commit()
