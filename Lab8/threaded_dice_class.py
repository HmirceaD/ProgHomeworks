import threading
from random import randint


class ThreadedDice(threading.Thread):

    dice_faces = ["one", "two", "three", "four", "five", "six"]

    def __init__(self):
        threading.Thread.__init__(self)

        self.dice_ascii = []

        for dice in self.dice_faces:
            with open("{}.txt".format(dice), "r") as f:
                self.dice_ascii.append(f.read())

    def run(self):
        print(self.dice_ascii[randint(0, 5)])
