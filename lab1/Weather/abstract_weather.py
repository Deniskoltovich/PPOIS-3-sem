from abc import ABC, abstractmethod

class BaseWeather(ABC):

    @abstractmethod
    def get_sunny(self): ...

    @abstractmethod
    def get_rainy(self): ...

    @abstractmethod
    def get_dry(self): ...

    @abstractmethod
    def get_cloudy(self): ...