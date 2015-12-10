from flask import Blueprint, render_template
from flask_login import current_user
from .models import sidebar_items, ceo_sidebar_items

basic = Blueprint('basic', __name__)


@basic.route('/')
def home():
    current_sidebar = sidebar_items

    if not current_user.is_anonymous and current_user.account_type_id == 1:
        current_sidebar = ceo_sidebar_items

    return render_template('home.html', sidebar_items=current_sidebar)
