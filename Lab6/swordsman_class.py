from soldier_class import Soldier


class Swordsman(Soldier):

    def __init__(self, weapon):
        super(Swordsman, self).__init__("Swordsman", 100, 50, True, 20)
        self.weapon = weapon

    def say_hurray(self):
        print("Your mother was a hamster and "
              "your father smelt of elderberries")