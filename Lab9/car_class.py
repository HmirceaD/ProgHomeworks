import threading
import random
import time


class Car(threading.Thread):

    def __init__(self, number , target, args):

        threading.Thread.__init__(self, target=target, args=args)
        self.number = number

    def run(self):

        super(Car, self).run()
        self.delay = random.randint(1, 5)
        time.sleep(self.delay)
        self.start_car()

        return

    def start_car(self):
        print("Car no. {} started after {} seconds".format(self.number, self.delay))
