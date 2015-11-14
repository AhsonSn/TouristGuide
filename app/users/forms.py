from wtforms import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


class LoginForm(Form):
    name = StringField('Felhasználónév', validators=[DataRequired()])
    pwd = PasswordField('Jelszó', validators=[DataRequired()])
    submit = SubmitField('Belépés')


class RegisterForm(Form):
    name = StringField('Felhasználónév', validators=[DataRequired()])
    email = StringField('E-mail cím', validators=[DataRequired(), Email()])
    pwd = PasswordField('Jelszó', validators=[DataRequired()])
    pwdRepeat = PasswordField('Jelszó újra', validators=[EqualTo(pwd)])
    submit = SubmitField('Regisztráció')
