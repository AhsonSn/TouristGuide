import requests


class Weather(object):
    def __init__(self, d):
        self.morn_temp = d["temp"]["morn"]
        self.day_temp = d["temp"]["day"]
        self.eve_temp = d["temp"]["eve"]
        self.night_temp = d["temp"]["night"]
        self.min_temp = d["temp"]["min"]
        self.max_temp = d["temp"]["max"]
        self.humidity = d["humidity"]
        self.main_weather = d["weather"][0]["main"]
        self.pressure = d["pressure"]
        self.clouds = d["clouds"]
        self.wind_speed = d["speed"]
        self.wind_degrees = d["deg"]

    def __str__(self):
        return "Main weather: {mw}\n" \
               "Temperature: morning: {m} day: {d} eve: {e} night: {n} min: {min} max: {max}\n" \
               "Humidity: {h}\nPressure: {p}\nClouds: {c}\n" \
               "Wind speed: {ws}\nWind degrees {wd}\n".format(
                                                            mw=self.main_weather,
                                                            m=self.morn_temp,
                                                            d=self.day_temp,
                                                            e=self.eve_temp,
                                                            n=self.night_temp,
                                                            min=self.min_temp,
                                                            max=self.max_temp,
                                                            h=self.humidity,
                                                            p=self.pressure,
                                                            c=self.clouds,
                                                            ws=self.wind_speed,
                                                            wd=self.wind_degrees)
