from field import Field
from ..Weather.weather import Weather


class BaseGarden:
    WEATHER = Weather()

    def __init__(self, fields: tuple[Field]):
        self._fields = fields

    def next_day(self):
        health_impact = self.WEATHER.is_sunny * 5
        hydro_impact = self.WEATHER.is_rainy * 5
        for field in self.fields:
            field.grow()
            field.plant.get_hydrated(hydro_impact)
            field.plant.health += health_impact

    @property
    def fields(self):
        return self._fields
