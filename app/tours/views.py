from flask import Blueprint, render_template
from ..basic.models import sidebar_items
from ..db.tourmanager import TourManager
from .forms import TourForm

tours_blueprint = Blueprint('tours', __name__)


@tours_blueprint.route('/tours', methods=('GET', 'POST'))
def tours():
    tour_form = TourForm()

    if tour_form.validate_on_submit():
        tours_per_page = tour_form.tours_per_page.data
        order_by = tour_form.order_by.data
    else:
        tours_per_page = tour_form.tours_per_page.choices[0][0]
        order_by = tour_form.order_by.choices[0][0]

    tour_list = TourManager.get_list_of_tours(tours_per_page, order_by)
    return render_template('tours.html', sidebar_items=sidebar_items,
                           tours=tour_list, tour_form=tour_form)
