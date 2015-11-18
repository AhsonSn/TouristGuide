from app import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(10), primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class Experience(db.Model):
    __tablename__ = 'experiences'

    id = db.Column(db.Integer(10), primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Experience %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(40), nullable=False)
    fullname = db.Column(db.Strin(64), nullable=False)
    avatarsrc = db.Column(db.String(100))
    birth = db.Column(db.Date)
    experience = db.Column(db.Integer(10), db.ForeignKey('experiences.id'))
    accounttype = db.Column(db.Integer(10), db.ForeignKey('roles.id'))
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer(11))

    def __repr__(self):
        return '<User %r>' % self.username


class Tour(db.Model):
    __tablename__ = 'tours'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    startdatetime = db.Column(db.DateTime)
    enddatetime = db.Column(db.DateTime)
    images = db.Column(db.String(1000))
    experience = db.Column(db.Integer(10), db.ForeignKey('experiences.id'))
    tourguidid = db.Column(db.Integer(10), db.ForeignKey('users.id'))
    description = db.Column(db.Strin(1000))

    def __repr__(self):
        return '<Tour %r>' % self.tourname


class Registration(db.Model):
    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True)
    tourid = db.Column(db.Integer(10), db.ForignKey('tours.id'), nullable=False)
    userid = db.Column(db.Integer(10), db.ForignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime)
    isPaid = db.Column(db.Boolean)

    def __repr__(self):
        return '<Registration %r>' % self.id
