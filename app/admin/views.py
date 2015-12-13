from flask import Blueprint, render_template, request
from flask_login import login_required
from .forms import AddTourForm, EditTourForm, StatisticsForm, EditTourGuidesForm
from ..basic.models import ceo_sidebar_items, sidebar_items
from ..db.experiencemanager import ExperienceDAO
from ..db.tourmanager import TourDAO
from ..db.usermanager import UserDAO
from ..statistics.statistics import Statistics

admin = Blueprint('admin', __name__)


@admin.route('/add-tour', methods=('GET', 'POST'))
@login_required
# CEO ONLY
def add_tour():
    add_tour_form = AddTourForm()
    add_tour_form.experience.choices = [(e.id, e.name) for e in
                                        ExperienceDAO.get_experiences()]

    add_tour_form.tour_guide.choices = [(guide.id, guide.fullname) for guide in
                                        UserDAO.get_user_by_role_id(4)]

    success = False

    if add_tour_form.validate_on_submit():
        TourDAO.insert_tour(add_tour_form)
        success = True

    return render_template('add-tour.html',
                           add_tour_form=add_tour_form,
                           sidebar_items=ceo_sidebar_items,
                           success=success)


@admin.route('/edit-tour/<int:tour_id>', methods=('GET', 'POST'))
@login_required
# CEO ONLY
def edit_tour(tour_id):
    current_tour = TourDAO.get_tour_by_id(tour_id)
    edit_tour_form = EditTourForm()

    edit_tour_form.experience.choices = [(e.id, e.name) for e in
                                         ExperienceDAO.get_experiences()]

    edit_tour_form.tour_guide.choices = [(guide.id, guide.fullname) for guide in
                                         UserDAO.get_user_by_role_id(4)]

    success = False

    if edit_tour_form.validate_on_submit():
        success = TourDAO.update_tour(current_tour, edit_tour_form)
    else:
        edit_tour_form.name.data = current_tour.name
        edit_tour_form.place.data = current_tour.place
        edit_tour_form.start_date.data = current_tour.start_datetime
        edit_tour_form.end_date.data = current_tour.end_datetime
        edit_tour_form.price.data = current_tour.price
        edit_tour_form.description.data = current_tour.description

    return render_template('tour-edit.html',
                           edit_tour_form=edit_tour_form,
                           sidebar_items=ceo_sidebar_items,
                           tour=current_tour,
                           experience=current_tour.experience_id,
                           guide=current_tour.tour_guide_id,
                           success=success)


@admin.route('/statistics', methods=('GET', 'POST'))
@login_required
# CEO ONLY
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
                               sidebar_items=ceo_sidebar_items,
                               chart_type=chart_type,
                               labels=labels,
                               data=data
                               )

    return render_template('statistics_form.html',
                           statistics_form=statistics_form,
                           sidebar_items=ceo_sidebar_items)


@admin.route('/tour_guide_edit', methods=('GET', 'POST'))
@login_required
# TOUR SUPERVISOR ONLY
def tour_leaders_edit():
    tour_guides = UserDAO.get_user_by_role_id(4)
    edit_tour_guides_form = EditTourGuidesForm()

    if edit_tour_guides_form.validate_on_submit():
        for tour_guide in tour_guides:
            status = int(request.form[str(tour_guide.id)])
            if status != tour_guide.status:
                UserDAO.update_status(tour_guide.id, status)

    return render_template('tourguide-edit.html',
                           edit_tour_guides_form=edit_tour_guides_form,
                           tour_guides=tour_guides,
                           sidebar_items=sidebar_items)
