from abc import abstractmethod

from lab1.Plants.abstract_plants import BasePlant


class Fruit(BasePlant):
    pass


class Vegetable(BasePlant): ...


class Tree(BasePlant):
    def __init__(self, health: int = 100,
                 hydration_level: int = 100, age: int = 0, fruit=None):
        self._fruit: None | Fruit = fruit
        super().__init__(health=health, hydration_level=hydration_level, age=age)

    def grow(self):
        if self.age > 5:
            self.create_fruit()
        super().grow()

    @abstractmethod
    def create_fruit(self):
        raise NotImplementedError

    @property
    def fruit(self):
        return self._fruit

    @fruit.setter
    def fruit(self, fruit: Fruit):
        self._fruit = fruit

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age
        if self.fruit:
            self.fruit.age = age - 5

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value
        if self._health > 100:
            self._health = 100
        if self.fruit:
            self.fruit.health = self.health

    @property
    def hydration_level(self):
        return self._hydration_level

    @hydration_level.setter
    def hydration_level(self, value: int):
        self._hydration_level = value
        if self.hydration_level > 100:
            self._hydration_level = 100
        if self.fruit:
            self.fruit.hydration_level = self.hydration_level

    def get_dehydrated(self, value: int = 15):
        self.hydration_level -= value
        if self.hydration_level <= 0:
            self.die()

    def get_hydrated(self, value: int = 15):
        self.hydration_level += value
