from flask import Blueprint, render_template
from .models import sidebar_items

basic = Blueprint('basic', __name__)


@basic.route('/')
def home():
    return render_template('home.html', sidebar_items=sidebar_items)
