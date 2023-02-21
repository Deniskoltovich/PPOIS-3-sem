from abc import ABC, abstractmethod

class BasePlant(ABC):

    @abstractmethod
    def grow(self): ...

    @abstractmethod
    def die(self): ...

    @abstractmethod
    def get_dehydrated(self): ...

    @abstractmethod
    def get_hydrated(self): ...