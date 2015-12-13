from flask_login import UserMixin

from app import database
from app import loginmanager


class Role(database.Model):
    def __init__(self, id_, name_):
        self.id = id_
        self.name = name_

    __tablename__ = 'roles'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)

    def __repr__(self):
        return '<Role \'{}\', id: {}>'.format(self.name, self.id)


class Experience(database.Model):
    """
    Values of this table: Könnyű, Közepes, Közepesen Nehéz, Nehéz
    """

    def __init__(self, id_, name_):
        self.id = id_
        self.name = name_

    __tablename__ = 'experiences'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id and self.name == other.name

        return False

    def __repr__(self):
        return '<Experience \'{}\', id: {}>'.format(self.name, self.id)


class User(UserMixin, database.Model):
    def __init__(self, name, pwd, email_):
        self.username = name
        self.password = pwd
        self.email = email_

    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(64), unique=True, index=True)
    password = database.Column(database.String(40), nullable=False)
    fullname = database.Column(database.String(64), nullable=False)
    avatar_src = database.Column(database.String(100))
    birth = database.Column(database.Date)

    experience_id = database.Column(
        database.Integer, database.ForeignKey('experiences.id'))

    experience = database.relationship(
        'Experience', backref=database.backref('users', lazy='dynamic')
    )

    account_type_id = database.Column(
        database.Integer, database.ForeignKey('roles.id')
    )

    account_type = database.relationship(
        'Role', backref=database.backref('users', lazy='dynamic')
    )

    email = database.Column(database.String(100), nullable=False)
    phone = database.Column(database.String(11))
    allowance = database.Column(database.Integer)
    numoftours = database.Column(database.Integer)
    status = database.Column(database.Integer)

    def __repr__(self):
        return '<User \'{}\'>'.format(self.username)


@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Tour(database.Model):
    def __init__(self, data):
        self.name = data['name']
        self.place = data['place']
        self.start_datetime = data['start_date']
        self.end_datetime = data['end_date']
        self.experience_id = data['experience']
        self.tour_guide_id = data['tour_guide']
        self.description = data['description']
        self.price = data['price']

    __tablename__ = 'tours'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), index=True)
    place = database.Column(database.String(64))
    start_datetime = database.Column(database.DateTime)
    end_datetime = database.Column(database.DateTime)
    images = database.Column(database.Text)

    experience_id = database.Column(
        database.Integer, database.ForeignKey('experiences.id')
    )

    experience = database.relationship(
        'Experience', backref=database.backref('tours', lazy='dynamic')
    )

    tour_guide_id = database.Column(
        database.Integer, database.ForeignKey('users.id')
    )

    tour_guide = database.relationship(
        'User', backref=database.backref('tours', lazy='dynamic')
    )

    description = database.Column(database.Text)

    price = database.Column(database.Integer)

    def __repr__(self):
        return '{}'.format(self.name)


class Registration(database.Model):
    def __init__(self, user, tour, date, paid):
        self.user = user
        self.tour = tour
        self.date = date
        self.isPaid = paid

    __tablename__ = 'registrations'

    id = database.Column(database.Integer, primary_key=True)

    tour_id = database.Column(
        database.Integer, database.ForeignKey('tours.id'), nullable=False
    )

    tour = database.relationship(
        'Tour', backref=database.backref('registrations', lazy='dynamic')
    )

    user_id = database.Column(
        database.Integer, database.ForeignKey('users.id'), nullable=False
    )

    user = database.relationship(
        'User', backref=database.backref('registrations', lazy='dynamic')
    )

    date = database.Column(database.DateTime)
    isPaid = database.Column(database.Boolean)

    def __repr__(self):
        return '<Registration \'{}\'>'.format(self.id)


class Message(database.Model):
    def __init__(self, from_user, subject_, message, date_):
        self.from_user_id = from_user
        self.subject = subject_
        self.message = message
        self.date = date_
        self.read = 0


    __tablename__ = 'messages'

    id = database.Column(database.Integer, primary_key=True)

    from_user_id = database.Column(
        database.Integer, database.ForeignKey('users.id'), nullable=False
    )

    from_user = database.relationship(
        'User', backref=database.backref('message', lazy='dynamic')
    )

    date = database.Column(database.DateTime, nullable=False)

    message = database.Column(database.Text)

    read = database.Column(database.Integer)

    subject = database.Column(database.Text)

    def __repr__(self):
        return '<Message \'{}\'>'.format(self.id)
