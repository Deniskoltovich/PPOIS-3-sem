from plant import Tree, Fruit


class AppleTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Apple()


class Apple(Fruit):
    ...


class PearTree(Tree):
    def create_fruit(self):
        if not self.fruit:
            self.fruit = Pear()


class Pear(Fruit):
    ...
