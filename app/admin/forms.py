from flask_wtf import Form
from wtforms import StringField, TextAreaField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class AddTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(AddTourForm, self).generate_csrf_token(csrf_context)

    name = StringField(
        u'Túra neve',
        validators=[DataRequired(u'Add meg a túra nevét!')]
    )

    start_date = DateField(
        u'Túra időpontja',
        validators=[DataRequired(u'Add meg a kezdődátumot!')]
    )

    end_date = DateField(
        u'-',
        validators=[DataRequired(u'Add meg a vég dátumot!')]
    )

    images = FileField(
        u'Túra képei',
        validators=[DataRequired(u'Adj meg legalább 1 képet')]
    )

    description = TextAreaField(
        u'Túra leírása',
        validators=[DataRequired(u'Add meg a túra leírását!')]
    )


class EditTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(EditTourForm, self).generate_csrf_token(csrf_context)

    name = StringField(u'Túra neve')
    description = TextAreaField(u'Túra leírása')
