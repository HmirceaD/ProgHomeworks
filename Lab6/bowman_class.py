from soldier_class import Soldier


class Bowman(Soldier):

    def __init__(self, weapon):
        super(Bowman, self).__init__("Bowman", 110, 30, False, 30)
        self.weapon = weapon

    def say_hurray(self):
        print("Nobody expects the spanish inquisition")
