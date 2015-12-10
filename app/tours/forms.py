from flask_wtf import Form
from wtforms import SubmitField, SelectField, StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import Optional


class TourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(TourForm, self).generate_csrf_token(csrf_context)

    order_by = SelectField(
        u'Rendezés',
        choices=[(1, 'Dátum'), (2, 'ABC'), (3, 'Tapasztalati szint')],
        coerce=int,
        default=1
    )

    tours_per_page = SelectField(
        u'Túrák oldalanként',
        choices=[(12, 12), (24, 24), (36, 36), (48, 48), (60, 60)],
        coerce=int,
        default=12
    )

    submit = SubmitField(u'Mehet')


class SearchTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(SearchTourForm, self).generate_csrf_token(csrf_context)

    place = StringField(u'Túra helyszíne', validators=[Optional()])
    date = DateField(u'Túra időpontja', validators=[Optional()])
    submit = SubmitField(u'Mehet')
