import requests
import datetime

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
            date = datetime.date(today.year, today.month, today.day + index)
            self.weathers[date] = Weather(data)

    def get_weather_by_date(self, date):
        return self.weathers[date]

    def get_weathers(self):
        result = ""
        for date in self.weathers:
            result += "Date: {d}\nWeather information:\n{wi}\n".format(d=date, wi=self.weathers[date])
        return result


def main():
    print(WeatherFactory("Debrecen", 2).get_weathers())


if __name__ == "__main__":
    main()
