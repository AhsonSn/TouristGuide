from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


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

    email = StringField(
        u'E-mail cím',
        validators=[
            DataRequired(u'Adj meg egy email címet!'),
            Email(u'Érvénytelen email cím!')
        ]
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

    submit = SubmitField(u'Regisztráció')
