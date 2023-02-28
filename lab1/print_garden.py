from Garden.field import Field
from Garden.garden import BaseGarden
from Plants.plant import BasePlant
from Plants.plant import Tree


def print_plant(plant: BasePlant):
    print(f'|\tAge: {plant.age}'.ljust(45),
          f'|\tHealth: {plant.health}'.ljust(45),
          f'|\tHydration level: {plant.hydration_level}'.ljust(45),
          f'|\tIllness damage: {plant.illness.destruction_power}'.ljust(45),
          f'|\tPests damage: {plant.pests.destruction_power}'.ljust(45), sep='|\n', end='|\n')


def print_field(field: Field):
    print('_' * 47)
    if field.plant is not None:
        print(f'|\tPlant: {field.plant}'.ljust(45), end='|\n')
        print_plant(field.plant)
    else:
        print(f'|\tPlant: Weed'.ljust(45),
              f'|\tHealth: {field.weed.health}'.ljust(45),
              sep='|\n', end='|\n')
    print('|' + '_' * 46 + '|')


def print_garden(garden: BaseGarden):
    i = 1
    print(f'Weather: {garden.WEATHER}')
    for field in garden.fields:
        print(f'{i}.')
        print_field(field)
        i += 1
