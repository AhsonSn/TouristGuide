from werkzeug.security import generate_password_hash
from .models import User, Role
from app import database
from .formextractor import FormExtractor


class UserManager(object):


    def insert_user_by_params(self, name, pwd, email, fullname, birth, avatar = "", experience_id=1, account_type_id=3 ):
        """
        Inserts a user to database, from the registration form.

        Password will not be stored in Database, only password sha1s.
        This method checks if a username or email is already in the database.
        If it does, this method returns False.
        If it doesn't, then adds a new user to the database.
        :param name: user name
        :param pwd: user password
        :param email: user email
        :param fullname: full name of user
        :param experience_id: experience in tour
        :param account_type_id: user type: CEO, tourguide, tourmanager, user
        :return: True if insert was succesed
        """

        passw = generate_password_hash(pwd)
        user = User(name, passw, email)
        user.account_type_id = account_type_id
        user.experience_id = experience_id
        user.fullname = fullname
        user.birth = birth
        user.avatar_src = avatar

        if UserManager.get_user_by_name(name) is not None \
                or UserManager.get_user_by_email(email) is not None:
            return False

        database.session.add(user)
        database.session.commit()
        return True

    def insert_user(self, form):
        """
        Insert a user by form.

        :param form:
        :return: None
        """
        data = FormExtractor.extract(form)
        self.insert_user_by_params(*data)


    def get_user_by_name(self, name):
        """
        Return a User instance where username is equal name.

        :param name: username
        :return: User instance
        """
        return User.query.filter_by(username=name).first()

    def get_user_by_email(self, email_):
        """
        Return a User instance where email is equal email.
        :param email_: Users emails
        :return: User instance
        """
        return User.query.filter_by(email=email_).first()

    def get_user_by_role(self, role_name):
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
