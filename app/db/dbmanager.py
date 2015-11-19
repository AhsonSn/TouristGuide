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
        self.db.session.add(user)
        self.db.session.commit()
