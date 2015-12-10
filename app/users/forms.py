from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField, BooleanField, \
    SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Optional


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
    remember_me = BooleanField('Jegyezzen meg')
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

    experience = SelectField(
        u'Tapasztalati szint (saját bevallás alapján)',
        coerce=int
    )

    birthDate = DateField(
        u'Születési dátum',
        validators=[DataRequired(u'Add meg a születési dátumodat!')]
    )

    phoneNumber = StringField(
        u'Telefonszám',
        validators=[Optional(),
                    Regexp("[0-9]{11}", message="Add meg a telefonszámodat!")]
    )

    avatar = FileField(
        u'Profilkép'
    )

    submit = SubmitField(u'Regisztráció')


class SettingsForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(SettingsForm, self).generate_csrf_token(csrf_context)

    name = StringField(
        u'Felhasználónév',
        validators=[DataRequired(u'Adj meg egy felhasználónevet!')]
    )

    new_pwd = PasswordField(
        u'új jelszó'
    )

    old_pwd = PasswordField(
        u'Jelenlegi jelszavad',
        validators=[
            DataRequired(u'Add meg a jelszavad a beállítások módosításához!')
        ]
    )

    email = StringField(
        u'E-mail cím',
        validators=[
            DataRequired(u'Adj meg egy email címet!'),
            Email(u'Érvénytelen email cím!')
        ]
    )

    experience = SelectField(
        u'Tapasztalati szint (saját bevallás alapján)',
        coerce=int
    )

    phoneNumber = StringField(
        u'Telefonszám',
        validators=[Optional(),
                    Regexp("[0-9]{11}", message="Érvénytelen telefonszám!")]
    )

    avatar = FileField(
        u'Profilkép'
    )

    submit = SubmitField(u'Beállítások mentése')
