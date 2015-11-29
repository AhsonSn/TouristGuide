from flask import Blueprint, render_template, redirect, url_for
from ..basic.models import sidebar_items
from ..db.tourmanager import TourManager
from .forms import TourForm

tours_blueprint = Blueprint('tours', __name__)
tours_blueprint.current_items_per_page = None
tours_blueprint.current_order_by = None


@tours_blueprint.route('/tours')
def tours_default():
    return redirect(url_for('.tours', current_page=1))


@tours_blueprint.route('/tours/<int:current_page>', methods=('GET', 'POST'))
def tours(current_page):
    tour_form = TourForm()

    if not tours_blueprint.current_items_per_page:
        tours_blueprint.current_items_per_page = tour_form.tours_per_page.default

    if not tours_blueprint.current_order_by:
        tours_blueprint.current_order_by = tour_form.order_by.default

    if tour_form.validate_on_submit():
        tours_blueprint.current_items_per_page = tour_form.tours_per_page.data
        tours_blueprint.current_order_by = tour_form.order_by.data

    pagination = TourManager.get_page_of_tours(
        current_page, tours_blueprint.current_items_per_page, tours_blueprint.current_order_by
    )

    return render_template('tours.html', sidebar_items=sidebar_items, tour_form=tour_form,
                           tours=pagination.items, pagination=pagination, items=tours_blueprint.current_items_per_page,
                           sort=tours_blueprint.current_order_by)
