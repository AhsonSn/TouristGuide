from app import database



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


class User(database.Model):
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
    phone = database.Column(database.Integer)

    def __repr__(self):
        return '<User \'{}\'>'.format(self.username)


class Tour(database.Model):
    __tablename__ = 'tours'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True, index=True)
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

    def __repr__(self):
        return '<Tour \'{}\'>'.format(self.tourname)


class Registration(database.Model):
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
