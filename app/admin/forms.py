from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class AddTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return Form.generate_csrf_token(csrf_context)

    name = StringField(
        u'Túra neve',
        validators=[DataRequired(u'Add meg a túra nevét!')]
    )

    description = TextAreaField(
        u'Túra leírása',
        validators=[DataRequired(u'Add meg a túra leírását!')]
    )


class EditTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return Form.generate_csrf_token(csrf_context)

    name = StringField(u'Túra neve')
    description = TextAreaField(u'Túra leírása')
