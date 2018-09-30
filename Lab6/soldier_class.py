class Soldier:

    def __init__(self, type, attack,
                 defense, armored, cost):

        self.type = type
        self.attack = attack
        self.defense = defense
        self.armored = armored
        self.cost = cost
        self.joined_army = None

    def join(self, player, army):
        """Join the army if the player has the money and the
        soldier isn't already in an army"""

        if player.get_amout() < self.cost:
            print("You don't have the money mate")
        else:
            if self.joined_army is None:
                player.amount -= self.cost
                army.list.append(self)
                self.joined_army = army
            else:
                print("I already joined an army")

    def say_hurray(self):
        pass

    def get_army(self):

        if self.joined_army is None:
            return "No army"
        else:
            return self.joined_army.name

    def get_type(self):
        return self.type

    def get_cost(self):
        return self.cost

    def die(self):
        print("Tis but a scratch")
        self.joined_army.list.remove(self)

    def fight(self, soldier):
        """The uml does not have the soldier attribute but
        I do not know how to implement this otherwise"""

        """if the soldier is armored he takes less
        damage but loses the armor after one hit"""
        if soldier.armored:
            soldier.defense -= self.attack / 2
            soldier.armored = False
        else:
            soldier.defense -= self.attack

    def acknowledge(self):
        """If the army is informed it makes it stronger"""
        self.attack += 15
