from flask import Blueprint, render_template
from flask_login import login_required

from .forms import AddTourForm, EditTourForm, StatisticsForm
from ..basic.models import sidebar_items
from ..db.experiencemanager import ExperienceManager
from ..db.tourmanager import TourManager
from ..db.usermanager import UserManager
from ..statistics.statistics import Statistics

admin = Blueprint('admin', __name__)


@admin.route('/add-tour', methods=('GET', 'POST'))
@login_required
# CEO ONLY
def add_tour():
    add_tour_form = AddTourForm()
    add_tour_form.experience.choices = [(e.id, e.name) for e in
                                        ExperienceManager.get_experiences()]

    add_tour_form.tour_guide.choices = [(guide.id, guide.fullname) for guide in
                                        UserManager.get_user_by_role_id(4)]

    success = False

    if add_tour_form.validate_on_submit():
        print(add_tour_form)
        TourManager.insert_tour(add_tour_form)
        success = True

    return render_template('add-tour.html',
                           add_tour_form=add_tour_form,
                           sidebar_items=sidebar_items,
                           success=success)


@admin.route('/edit-tour', methods=('GET', 'POST'))
@login_required
def edit_tour():
    edit_tour_form = EditTourForm()

    if edit_tour_form.validate_on_submit():
        return 'Success'

    return render_template('tour-edit.html',
                           edit_tour_form=edit_tour_form,
                           sidebar_items=sidebar_items)


@admin.route('/statistics', methods=('GET', 'POST'))
def statistics():
    statistics_form = StatisticsForm()

    if statistics_form.validate_on_submit():
        stat = Statistics()
        chart_type = "bar_chart"
        if statistics_form.input_type.data == "reg_user":
            (labels, data) = stat.get_stat_by_registered_user(statistics_form.start_date.data,
                                                              statistics_form.end_date.data)
        elif statistics_form.input_type.data == "guided_tour":
            (labels, data) = stat.get_stat_by_tourguide(statistics_form.start_date.data,
                                                        statistics_form.end_date.data)
        elif statistics_form.input_type.data == "popularity":
            (labels, data) = stat.get_stat_by_tourguide_popularity(statistics_form.start_date.data,
                                                                   statistics_form.end_date.data)
        return render_template('statistics.html',
                               statistics_form=statistics_form,
                               sidebar_items=sidebar_items,
                               chart_type=chart_type,
                               labels=labels,
                               data=data
                               )

    return render_template('statistics_form.html',
                           statistics_form=statistics_form,
                           sidebar_items=sidebar_items)
