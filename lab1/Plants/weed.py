class Weed:
    def __init__(self):
        self._health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int=100):
        self._health = value




