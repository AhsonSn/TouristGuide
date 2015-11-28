from flask_wtf import Form
from wtforms import SubmitField, SelectField


class TourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(TourForm, self).generate_csrf_token(csrf_context)

    order_by = SelectField(
        u'Rendezés',
        choices=[(1, 'Dátum'), (2, 'ABC'), (3, 'Tapasztalati szint')],
        coerce=int
    )

    tours_per_page = SelectField(
        u'Túrák oldalanként',
        choices=[(12, 12), (24, 24), (36, 36), (48, 48), (60, 60)],
        coerce=int
    )

    submit = SubmitField(u'Mehet')
