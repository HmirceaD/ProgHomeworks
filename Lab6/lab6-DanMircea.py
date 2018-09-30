from army_class import Army
from bowman_class import Bowman
from player_class import Player
from scouter_class import Scouter
from swordsman_class import Swordsman

army_red = Army("Red Army", [])
army_black = Army("Red Army", [])

player_one = Player(1000, army_red)
player_two = Player(100, army_black)

bowman_1 = Bowman("Arc smecher")
bowman_2 = Bowman("Arc mai putin smecher")
scouter_1 = Scouter("Papuci")

scouter_1.join(player_one, army_red)
bowman_1.join(player_one, army_red)
bowman_2.join(player_one, army_red)
bowman_1.say_hurray()

scouter_1.inform_army(army_red)

swordman = Swordsman("Sabie de carton")
bowman_3 = Bowman("Elastic")
swordman.say_hurray()

swordman.join(player_two, army_black)
bowman_3.join(player_two, army_black)

army_red.fight(army_black)






