#=====prob4
import threading
import sys


class CardPackage:

    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
    colors = ["heart", "diamond", "spade", "club"]

    def get_package(self):

        card_package = []

        for number in self.card_values:
            for color in self.colors:
                card_package.append("{0} of {1}".format(number, color))

        return card_package


class PokerPlayer(threading.Thread):

    def __init__(self, name, cards):
        threading.Thread.__init__(self)
        self.name = name
        self.cards = cards

    def run(self):
        self.get_cards()

    def get_cards(self):

        sys.stdout.write("\nI am {} and I had ".format(self.name))

        for card in self.cards:
            sys.stdout.write(" a {}".format(card))
