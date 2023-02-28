import random
from abc import ABC, abstractmethod
from math import floor


class AbstractPlant(ABC):

    @abstractmethod
    def grow(self):
        raise NotImplementedError

    @abstractmethod
    def die(self):
        raise NotImplementedError

    @abstractmethod
    def get_dehydrated(self):
        raise NotImplementedError

    @abstractmethod
    def get_hydrated(self):
        raise NotImplementedError


class Illness:
    def __init__(self):
        self._destruction_power = random.randint(10, 20)

    @property
    def destruction_power(self):
        return self._destruction_power

    @destruction_power.setter
    def destruction_power(self, value: int):
        self._destruction_power = value


class Pests:
    def __init__(self):
        self._destruction_power = random.randint(10, 20)

    @property
    def destruction_power(self):
        return self._destruction_power

    @destruction_power.setter
    def destruction_power(self, value: int):
        self._destruction_power = value


class BasePlant(AbstractPlant):
    def __init__(self, health: int = 100,
                 hydration_level: int = 100, age: int = 0):
        self.illness = Illness()
        self._age = age
        self._health = health
        self._hydration_level = hydration_level
        self._dead = False
        self.pests = Pests()
        if random.randint(1, 4) == 1:
            self.pests.destruction_power = 0
        if random.randint(1, 4) == 2:
            self.illness.destruction_power = 0

    def grow(self):
        self.age += 1
        if self.hydration_level > 50:
            impact = floor(self.hydration_level * .1) \
                     - self.illness.destruction_power - self.pests.destruction_power
            self.health += impact
        else:
            self.health -= abs(
                floor(self.hydration_level * .1)) + self.illness.destruction_power + self.pests.destruction_power
        self.get_dehydrated()
        if self.health <= 0:
            self.die()

    def die(self):
        self._dead = True

    @property
    def dead(self):
        return self._dead

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value
        if self._health > 100:
            self._health = 100

    @property
    def hydration_level(self):
        return self._hydration_level

    @hydration_level.setter
    def hydration_level(self, value: int):
        self._hydration_level = value
        if self._hydration_level > 100:
            self._hydration_level = 100

    def get_dehydrated(self, value: int = 15):
        self.hydration_level -= value
        if self.hydration_level <= 0:
            self.die()

    def get_hydrated(self, value: int = 15):
        self.hydration_level += value

    def __str__(self):
        return self.__class__.__name__
