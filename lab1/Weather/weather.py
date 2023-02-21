import random

from .abstract_weather import BaseWeather

class Weather(BaseWeather):
    def __init__(self):
        self._is_sunny: bool = random.choice([True, False])
        self._is_rainy: bool = random.choice([True, False])

    @property
    def is_sunny(self):
        return self._is_sunny

    @property
    def is_rainy(self):
        return self._is_rainy



