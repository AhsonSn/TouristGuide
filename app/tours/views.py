from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from .forms import TourForm
from ..basic.models import sidebar_items
from ..db.tourmanager import TourManager

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
        tours_blueprint.current_items_per_page = \
            tour_form.tours_per_page.default

    if not tours_blueprint.current_order_by:
        tours_blueprint.current_order_by = tour_form.order_by.default

    if tour_form.validate_on_submit():
        tours_blueprint.current_items_per_page = tour_form.tours_per_page.data
        tours_blueprint.current_order_by = tour_form.order_by.data
        return redirect(url_for('tours.tours_default'))

    pagination = TourManager.get_page_of_tours(
        current_page, tours_blueprint.current_items_per_page,
        tours_blueprint.current_order_by
    )

    return render_template('tours.html', sidebar_items=sidebar_items,
                           tour_form=tour_form,
                           tours=pagination.items, pagination=pagination,
                           items=tours_blueprint.current_items_per_page,
                           sort=tours_blueprint.current_order_by)


@tours_blueprint.route('/view-tour/<int:tour_id>')
def view_tour(tour_id):
    tour = TourManager.get_tour_by_id(tour_id)
    return render_template('tour-view.html', sidebar_items=sidebar_items,
                           tour=tour)


@tours_blueprint.route('/update-tour-images/<int:id_>/<string>')
@login_required
def update_tour_images(id_, string):
    if current_user.account_type_id == 1:
        TourManager.update_images(TourManager.get_tour_by_id(id_), string)
        return '1'
    else:
        return u'Hozzáfárás megtagadva'
