from thread_sort_class import ThreadSort
from threaded_dice_class import ThreadedDice
from threaded_char_count import ThreadedCharCount
from poker_class import PokerPlayer
from poker_class import CardPackage
import random
from queue import Queue

#=====prob1====
list1 = [5, 2, 7, 1, 9, 9]
list2 = [6, 4, 6, 1, 9, 3, 5, 9, 4]
list3 = [8, 2, 4, 1, 7, 4, 8, 0]

thread_obj = ThreadSort(list1, list2, list3)
thread_obj.start()
#=====

#=====prob2

dice1 = ThreadedDice()
dice2 = ThreadedDice()
dice3 = ThreadedDice()
dice4 = ThreadedDice()

dice1.start()
dice2.start()
dice3.start()
dice4.start()

#=====

#=====prob3=====

char_thread1 = ThreadedCharCount("e")
char_thread2 = ThreadedCharCount("a")
char_thread3 = ThreadedCharCount("w")

char_thread1.start()
char_thread2.start()
char_thread3.start()

#=====

#=====prob4=====

card_package = CardPackage().get_package()

random.shuffle(card_package)

card_queue = Queue()

for i in range(4):
    rand = random.randint(0, len(card_package) - 6)
    card_queue.put(card_package[rand:rand+5])

player1 = PokerPlayer("1", card_queue.get())
player2 = PokerPlayer("2", card_queue.get())
player3 = PokerPlayer("3", card_queue.get())
player4 = PokerPlayer("4", card_queue.get())

player1.start()
player2.start()
player3.start()
player4.start()

#=====