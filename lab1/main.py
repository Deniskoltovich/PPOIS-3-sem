from Plants.plant import Tree, Fruit, Vegetable
from Plants.trees import AppleTree, PearTree
from Garden.field import Field, FieldAction
from Garden.garden import BaseGarden
field_collection = [Field(AppleTree()), Field(PearTree()), Field(Vegetable())]

def main():
    garden = BaseGarden(field_collection)
    garden.next_day()
    garden.fields[1] = FieldAction(garden.fields[1]).hydrate_field()
    garden.next_day()
    garden.next_day()
    garden.fields[1] = FieldAction(garden.fields[1]).hydrate_field()


if __name__ == '__main__':
    main()
