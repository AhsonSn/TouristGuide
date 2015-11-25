import requests


def get_dailyweather(d):
    """
    Az OpenWeatherMap API által nyújtott JSON fájlból kinyeri egy NAP időjárását.
    :param d: egy napot reprezentáló dictionary
    :return: egy tuple, ami a következőkből áll temp dictionary, pressure, humidity, main weather
    """""
    return d["temp"], d["pressure"], d["humidity"], d["weather"][0]["main"]


def get_dailyweathers(d):
    """
    Az OpenWeatherMap API által nyújtott JSON fájlból kinyeri a napok időjárását.
    :param d: több napot reprezentáló dictionary
    :return: egy lista, ami naponkénti időjárás információkat tartalmaz
    """
    result = []
    for day in d["list"]:
        result.append(get_dailyweather(day))
    return result


class Weather(object):
    _apikey = 'cb2c8163bbd84861b2604df05eaaddf9'

    def __init__(self, city, day):
        self.city = city
        self.number_of_day = day
        self.get_weather()

    def get_weather(self):
        response = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={days}&APPID={apikey}".format(
                city=self.city, days=self.number_of_day, apikey=Weather._apikey))
        data = response.json()
        return get_dailyweathers(data)


def main():
    w = Weather('Debrecen', 14)
    print(w.get_weather())


if __name__ == "__main__":
    main()
