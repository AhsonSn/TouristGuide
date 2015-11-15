from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(Form):
    def generate_csrf_token(self, csrf_context):
        pass

    name = StringField(u'Felhasználónév', validators=[DataRequired()])
    pwd = PasswordField(u'Jelszó', validators=[DataRequired()])
    submit = SubmitField(u'Belépés')


class RegisterForm(Form):
    def generate_csrf_token(self, csrf_context):
        pass

    name = StringField(u'Felhasználónév', validators=[DataRequired()])
    email = StringField(u'E-mail cím', validators=[DataRequired(), Email()])
    pwd = PasswordField(u'Jelszó', validators=[DataRequired()])
    pwdRepeat = PasswordField(u'Jelszó újra', validators=[EqualTo(pwd)])
    submit = SubmitField(u'Regisztráció')
