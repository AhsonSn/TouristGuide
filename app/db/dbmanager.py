from werkzeug.security import generate_password_hash

class DBManager(object):
    def __init__(self):
        from app import database
        self.db = database

    def insert_user(self, form):
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
        from app.db.models import User
        user = User.query.filter_by(username=name).first()
        return user

    def get_user_by_email(self, email_):
        from app.db.models import User
        user = User.query.filter_by(email=email_).first()
        return user

    def get_experiences(self):
        from app.db.models import Experience
        exps = Experience.query.all()
        return exps