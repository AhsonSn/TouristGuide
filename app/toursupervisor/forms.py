from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class WeatherForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(WeatherForm, self).generate_csrf_token(csrf_context)

    city = StringField(
        u'Város neve',
        validators=[DataRequired(u'Kérem adjon meg egy városnevet!')]
    )
    numberOfDays = IntegerField(
        u'Napok száma',
        validators=[NumberRange(1, 16, u'Csak 1 és 16 közötti értéket adhat meg!')]
    )
    submit = SubmitField(u'Időjárás lekérdezése')
