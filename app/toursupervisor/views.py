from flask import Blueprint, render_template
from ..basic.models import sidebar_items

from .forms import WeatherForm

toursupervisor = Blueprint('toursupervisor', __name__)


@toursupervisor.route('/weather', methods=('GET', 'POST'))
def get_weather():
    weather_form = WeatherForm()
    return render_template('weather.html', weather_form=weather_form,
                           sidebar_items=sidebar_items)
