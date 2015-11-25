from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp
from flask_wtf.file import FileField


class LoginForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(LoginForm, self).generate_csrf_token(csrf_context)

    name = StringField(
        u'Felhasználónév',
        validators=[DataRequired(u'Adj meg egy felhasználónevet!')]
    )
    pwd = PasswordField(
        u'Jelszó',
        validators=[DataRequired(u'Adj meg egy jelszót!')]
    )
    submit = SubmitField(u'Belépés')


class RegisterForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(RegisterForm, self).generate_csrf_token(csrf_context)

    name = StringField(
        u'Felhasználónév',
        validators=[DataRequired(u'Adj meg egy felhasználónevet!')]
    )

    pwd = PasswordField(
        u'Jelszó',
        validators=[DataRequired(u'Adj meg egy jelszót!')]
    )

    pwdRepeat = PasswordField(
        u'Jelszó újra',
        validators=[
            DataRequired(),
            EqualTo('pwd', u'A jelszavak nem egyeznek meg!')
        ]
    )

    email = StringField(
        u'E-mail cím',
        validators=[
            DataRequired(u'Adj meg egy email címet!'),
            Email(u'Érvénytelen email cím!')
        ]
    )

    fullName = StringField(
        u'Teljes név',
        validators=[DataRequired(u'Add meg a teljes nevedet!')]
    )

    birthDate = DateField(
        u'Születési dátum',
        validators=[DataRequired(u'Add meg a születési dátumodat!')]
    )

    phoneNumber = StringField(
        u'Telefonszám',
        validators=[Regexp("[0-9]{11}", message="Add meg a telefonszámodat!")]
    )

    avatar = FileField(
        u'Profilkép'
    )

    submit = SubmitField(u'Regisztráció')
