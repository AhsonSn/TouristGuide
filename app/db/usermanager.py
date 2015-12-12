from sqlalchemy import update
from werkzeug.security import generate_password_hash

from .formextractor import FormExtractor
from .models import User, Role
from .. import database
from ..basic.models import UploadManager


class UserDAO(object):
    @staticmethod
    def insert_user(form, experience_id=1, account_type_id=3):
        """
        Inserts a user to database, from the registration form.

        Password will not be stored in Database, only password sha1s.
        This method checks if a username or email is already in the database.
        If it does, this method returns False.
        If it doesn't, then adds a new user to the database.
        :param form: the registration form object
        :param experience_id: experience in tour
        :param account_type_id: user type: CEO, tourguide, tourmanager, user
        :return: True if insert was successful
        """

        extr = FormExtractor.extract(form)
        passw = generate_password_hash(extr["pwd"])
        user = User(extr["name"], passw, extr["email"])
        user.account_type_id = account_type_id
        user.experience_id = experience_id
        user.fullname = extr["fullName"]
        user.birth = extr["birth"]
        user.phone = extr["phone"]

        if extr["avatar"]:
            user.avatar_src = UploadManager.upload_avatar(extr["avatar"])
        else:
            user.avatar_src = None

        if UserDAO.get_user_with_name(extr["name"]) is not None \
                or UserDAO.get_user_by_email(extr["email"]) is not None:
            return False

        database.session.add(user)
        database.session.commit()
        return True

    @staticmethod
    def get_user_by_id(id_):
        return User.query.get(id_)

    @staticmethod
    def get_user_with_name(name):
        """
        Return a User instance where username is equal name.

        :param name: username
        :return: User instance
        """
        return User.query.filter_by(username=name).first()

    @staticmethod
    def get_user_by_name(form):
        return UserDAO.get_user_with_name(
            FormExtractor.extract(form)["name"])

    @staticmethod
    def get_user_by_email(email_):
        """
        Return a User instance where email is equal email.
        :param email_: Users emails
        :return: User instance
        """
        return User.query.filter_by(email=email_).first()

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
    def get_user_by_role_id(role_id):
        return User.query.filter_by(
            account_type_id=role_id
        ).order_by(User.fullname).all()

    @staticmethod
    def update_username(id_, new_username):
        """
        Update the password of user.

        :param id_: id of user
        :param new_username: new username
        :return: True if it was updated
        """
        act_user = User.query.get(id_)

        if act_user is not None:
            up = update(User).where(User.id == id_).values(
                username=new_username
            )
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def update_pwd(username_, newpwd):
        """
        Update the password of user.

        :param username_: username of user
        :param newpwd: new password of username
        :return: True if it was updated
        """
        act_user = UserDAO.get_user_with_name(username_)

        if act_user:
            up = update(User).where(
                User.username == username_).values(
                password=generate_password_hash(newpwd)
            )
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def update_phone(username_, phonenumber):
        act_user = UserDAO.get_user_with_name(username_)

        if act_user:
            up = update(User).where(User.username == username_).values(
                phone=phonenumber
            )
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def update_avatar(username_, image):
        """
        Update avatar by user name.
        :param username_: username of user
        :param image: new user avatar image
        :return: True if update was succeed.
        """
        act_user = UserDAO.get_user_with_name(username_)

        if act_user:
            filename = UploadManager.upload_avatar(image)
            up = update(User).where(User.username == username_).values(
                avatar_src=filename)
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def update_email(username_, email):
        """
        Update email by username.
        :param username_: username of user
        :param email: new email of user
        :return: True if update was succeed
        """
        act_user = UserDAO.get_user_with_name(username_)

        if act_user is not None:
            up = update(User).where(User.username == username_).values(
                email=email)
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def update_experience(username_, exp_):
        """
        Update experience of username.
        :param username_: username of user
        :param exp_: experience id
        :return: True if update was succeed
        """
        act_user = UserDAO.get_user_with_name(username_)

        if act_user:
            up = update(User).where(User.username == username_).values(
                experience_id=exp_
            )
            database.session.execute(up)
            database.session.commit()
            return True

        return False

    @staticmethod
    def set_allowance(list_of_user):
        for user in list_of_user:
            up = update(User).where(User.id == user.id).values(
                allowance=user.allowance)
            database.session.execute(up)
            database.session.commit()

        return True
