from flask_wtf import Form
from wtforms import StringField, TextAreaField, FileField, SubmitField, \
    SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class AddTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(AddTourForm, self).generate_csrf_token(csrf_context)

    name = StringField(
        u'Túra neve',
        validators=[DataRequired(u'Add meg a túra nevét!')]
    )

    place = StringField(
        u'Túra helyszíne',
        validators=[DataRequired(u'Add meg a túra helyszínét!')]
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

    experience = SelectField(
        u'Szükséges tapasztalati szint', coerce=int
    )

    tour_guide = SelectField(
        u'Túravezető', coerce=int
    )

    description = TextAreaField(
        u'Túra leírása',
        validators=[DataRequired(u'Add meg a túra leírását!')]
    )

    price = IntegerField(
        u'Túra részvételi díja',
        validators=[DataRequired(u'Add meg a túra részvételi díját')]
    )

    submit = SubmitField(u'Túra létrehozása')


class EditTourForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(EditTourForm, self).generate_csrf_token(csrf_context)

    name = StringField(u'Túra neve')

    place = StringField(
        u'Túra helyszíne',
        validators=[DataRequired(u'Add meg a túra helyszínét!')]
    )

    start_date = DateField(
        u'Túra időpontja',
        validators=[DataRequired(u'Add meg a kezdődátumot!')]
    )

    end_date = DateField(
        u'-',
        validators=[DataRequired(u'Add meg a vég dátumot!')]
    )

    experience = SelectField(
        u'Szükséges tapasztalati szint', coerce=int
    )

    tour_guide = SelectField(
        u'Túravezető', coerce=int
    )

    description = TextAreaField(
        u'Túra leírása',
        validators=[DataRequired(u'Add meg a túra leírását!')]
    )

    price = IntegerField(
        u'Túra részvételi díja',
        validators=[DataRequired(u'Add meg a túra részvételi díját')]
    )

    submit = SubmitField(u'Túra mentése')


class StatisticsForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(StatisticsForm, self).generate_csrf_token(csrf_context)

    start_date = DateField(
        u'Adja meg a statisztika időintervallumának kezdő dátumát',
        validators=[DataRequired(u'Add meg a kezdődátumot!')]
    )

    end_date = DateField(
        u'Adja meg a statisztika befejező dátumát',
        validators=[DataRequired(u'Add meg a vég dátumot!')]
    )

    input_type = SelectField(u'Statisztika típusa',
                             choices=[('reg_user',
                                       'Regisztrált felhasználók száma szerint'),
                                      ('guided_tour',
                                       'A túravezetők által vezett túrák száma alapján'),
                                      ('popularity',
                                       'A túravezetők népszerűsége alapján')])

    submit = SubmitField(u'Diagram készítése')


class EditTourGuidesForm(Form):
    def generate_csrf_token(self, csrf_context=None):
        return super(EditTourGuidesForm, self).generate_csrf_token(csrf_context)

    submit = SubmitField(u'Mentés')
