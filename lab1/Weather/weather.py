import random

from lab1.Weather.abstract_weather import BaseWeather


class Weather(BaseWeather):
    def __init__(self):
        self._is_sunny: bool = random.choice([True, False])
        self._is_rainy: bool = True if random.randint(1, 4) == 2 else False

    def next_day(self):
        self.is_sunny: bool = random.choice([True, False])
        self.is_rainy: bool = True if random.randint(1, 4) == 2 else False

    @property
    def is_sunny(self):
        return self._is_sunny

    @property
    def is_rainy(self):
        return self._is_rainy

    @is_sunny.setter
    def is_sunny(self, value: bool):
        self._is_sunny = value

    @is_rainy.setter
    def is_rainy(self, value: bool):
        self._is_rainy = value
