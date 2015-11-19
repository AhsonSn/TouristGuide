from flask import Blueprint, render_template

from app.admin.forms import AddTourForm, EditTourForm
from app.basic.models import sidebar_items

admin = Blueprint('admin', __name__)


@admin.route('/add-tour', methods=('GET', 'POST'))
def add_tour():
    add_tour_form = AddTourForm()

    return render_template('add-tour.html',
                           add_tour_form=add_tour_form,
                           sidebar_items=sidebar_items,
                           success=True if add_tour_form.validate_on_submit()
                           else False)


@admin.route('/edit-tour', methods=('GET', 'POST'))
def edit_tour():
    edit_tour_form = EditTourForm()

    if edit_tour_form.validate_on_submit():
        return 'Success'

    return render_template('edit-tour.html',
                           edit_tour_form=edit_tour_form,
                           sidebar_items=sidebar_items)
