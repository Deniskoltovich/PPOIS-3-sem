import random
from abc import abstractmethod
from ..Plants.abstract_plants import BasePlant


class Field:
    def __init__(self, plants_collection: list[BasePlant]):
        self.plant = random.choice(plants_collection )
        self.weed = random.choice([True, False])
