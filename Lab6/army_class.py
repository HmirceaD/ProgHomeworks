from itertools import product
import random


class Army:

    def __init__(self, name, list1):
        self.name = name
        self.list = list1

    def fight(self, army):
        """each soldier from each army should have a turn
        at attacking a random enemy"""
        for i, j in product(range(len(self.list)),
                            range(len(army.list))):

            self.attack_enemy(self.list, army.list, i)
            self.attack_enemy(army.list, self.list, j)

    def attack_enemy(self, army_list, enemy_list, index):
        """each soldier should acquire a valid target and the attack it"""

        if index < len(army_list):
            """Obs: itertool.product continues until each index has reached end, if one 
            has reached the end, and the other didn't than it will continue with both
            regardless"""
            enemy_player = self.get_enemy(enemy_list)

            if enemy_player is not None:
                army_list[index].fight(enemy_player)
            else:
                print("Everybody on the enemy team died")

    def get_enemy(self, ls):
        """Keep searching until you get a valid target,
        and kill invalid ones"""
        try:
            enemy_player = ls[random.randint(0,len(ls)-1)]

            while enemy_player.defense < 0:
                enemy_player.die()
                enemy_player = ls[random.randint(0,len(ls)-1)]

            return enemy_player

        except (ValueError, IndexError):
            return None


