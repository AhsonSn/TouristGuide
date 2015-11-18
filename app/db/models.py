from app import database


class Role(database.Model):
    __tablename__ = 'roles'

    id = database.Column(database.Integer(), primary_key=True)
    name = database.Column(database.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class Experience(database.Model):
    __tablename__ = 'experiences'

    id = database.Column(database.Integer(), primary_key=True)
    name = database.Column(database.String(64), unique=True)

    def __repr__(self):
        return '<Experience %r>' % self.name


class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(64), unique=True, index=True)
    password = database.Column(database.String(40), nullable=False)
    fullname = database.Column(database.String(64), nullable=False)
    avatarsrc = database.Column(database.String(100))
    birth = database.Column(database.Date)
    experience = database.Column(database.Integer(10), database.ForeignKey('experiences.id'))
    accounttype = database.Column(database.Integer(10), database.ForeignKey('roles.id'))
    email = database.Column(database.String(100), nullable=False)
    phone = database.Column(database.Integer(11))

    def __repr__(self):
        return '<User %r>' % self.username


class Tour(database.Model):
    __tablename__ = 'tours'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True, index=True)
    startdatetime = database.Column(database.DateTime)
    enddatetime = database.Column(database.DateTime)
    images = database.Column(database.String(1000))
    experience = database.Column(database.Integer(10), database.ForeignKey('experiences.id'))
    tourguidid = database.Column(database.Integer(10), database.ForeignKey('users.id'))
    description = database.Column(database.Strin(1000))

    def __repr__(self):
        return '<Tour %r>' % self.tourname


class Registration(database.Model):
    __tablename__ = 'registrations'

    id = database.Column(database.Integer, primary_key=True)
    tourid = database.Column(database.Integer(10), database.ForignKey('tours.id'), nullable=False)
    userid = database.Column(database.Integer(10), database.ForignKey('users.id'), nullable=False)
    date = database.Column(database.DateTime)
    isPaid = database.Column(database.Boolean)

    def __repr__(self):
        return '<Registration %r>' % self.id
