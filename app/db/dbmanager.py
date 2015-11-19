from werkzeug.security import generate_password_hash


class DBManager(object):
    def __init__(self):
        """
        Reference database which in app.
        :return:
        """
        from app import database
        self.db = database

    def insert_user(self, form):
        """
        Insert a user to database, from the registration form.

        Password will not be stored in Database, only password sh1's case.
        This method check if a username or email is in the database. If contains, this method return False.
        If not, then user add to database.
        :param form: a form which contains name, email, pwd
        :return: True if success and False if not success
        """
        passw = generate_password_hash(form.pwd.data)
        n = form.name.data
        e = form.email.data
        from app.db.models import User
        user = User(n, passw, e)
        user.account_type_id = 3
        user.experience_id = 1
        user.fullname = ""

        if self.get_user_by_name(n) is not None or self.get_user_by_email(e) is not None:
            return False

        self.db.session.add(user)
        self.db.session.commit()
        return True

    def get_user_by_name(self, name):
        """
        Return a User instance where username is equal name.
        :param name: username
        :return: User instance
        """
        from app.db.models import User
        user = User.query.filter_by(username=name).first()
        return user

    def get_user_by_email(self, email_):
        """
        Return a User instance where email is equal email.
        :param email_: Users emails
        :return: User instance
        """
        from app.db.models import User
        user = User.query.filter_by(email=email_).first()
        return user

    def get_experiences(self):
        """
        Return a list of Experience from database.
        :return: list of Experience
        """
        from app.db.models import Experience
        exps = Experience.query.all()
        return exps
