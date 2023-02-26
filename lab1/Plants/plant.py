from abstract_plants import BasePlant
from abc import abstractmethod


class Fruit(BasePlant):
    pass


class Vegetable(BasePlant):
    pass


class Tree(BasePlant):
    def __init__(self):
        self._fruit: None | Fruit = None
        super().__init__()

    def grow(self):
        if self.age > 5:
            self.create_fruit()
        super().__init__()

    @abstractmethod
    def create_fruit(self):
        raise NotImplementedError

    @property
    def fruit(self):
        return self._fruit

    @fruit.setter
    def fruit(self, fruit: Fruit):
        self._fruit = fruit
