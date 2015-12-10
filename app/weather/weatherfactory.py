import requests
import datetime
import collections

from app.weather.weather import Weather


class WeatherFactory(object):
    _apikey = 'cb2c8163bbd84861b2604df05eaaddf9'

    def __init__(self, city, number_of_days):
        self.city = city
        self.number_of_days = number_of_days
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&units=metric&cnt={days}&APPID={apikey}".format(
                city=self.city, days=self.number_of_days, apikey=WeatherFactory._apikey))
        self.weathers = {}
        today = datetime.date.today()
        d = response.json()
        for index, data in enumerate(d["list"]):
            date = str(datetime.date(today.year, today.month, today.day + index))
            date = date[date.find('-') + 1:].replace('-', '.')
            self.weathers[date] = Weather(data)

    def get_weather_by_date(self, date):
        return self.weathers[date]

    def get_weathers(self):
        return collections.OrderedDict(sorted(self.weathers.items()))


def main():
    print(WeatherFactory("Debrecen", 2).get_weathers())


if __name__ == "__main__":
    main()
