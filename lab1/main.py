from Garden.field import Field, FieldAction
from Garden.garden import BaseGarden
from Plants.plant import Vegetable
from Plants.trees import AppleTree, PearTree
from print_garden import print_garden
from serializers import field_serializer, write_state, load_state

field_collection = [Field(AppleTree()), Field(PearTree()), Field(Vegetable())]


def main():
    garden = load_state()
    print_garden(garden)



if __name__ == '__main__':
    main()
