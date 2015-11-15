from flask import Blueprint, render_template
from html5print import HTMLBeautifier

from app.basic.models import sidebar_items

basic = Blueprint('basic', __name__)


@basic.route('/')
def home():
    return HTMLBeautifier.beautify(
        render_template('home.html', sidebar_items=sidebar_items), 2)


@basic.route('/tours')
def tours():
    return HTMLBeautifier.beautify(
        render_template('tours.html', sidebar_items=sidebar_items), 2)
