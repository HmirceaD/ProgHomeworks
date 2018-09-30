from soldier_class import Soldier


class Scouter(Soldier):

    def __init__(self, weapon):
        super(Scouter, self).__init__("Scouter", 50, 20, False, 15)
        self.weapon = weapon

    def say_hurray(self):
        print("Excelsior!")

    def inform_army(self, army):

        for soldier in army.list:
            soldier.acknowledge()
            print("I was informed by the scouter")