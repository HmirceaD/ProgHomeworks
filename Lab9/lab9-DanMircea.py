from car_class import Car
import threading
import time

#====prob1


def wait_semaphor(event):
    event.wait()


semaphor = threading.Event()
car1 = Car(1, wait_semaphor, (semaphor,))
car2 = Car(2, wait_semaphor, (semaphor,))
car3 = Car(3, wait_semaphor, (semaphor,))
car4 = Car(4, wait_semaphor, (semaphor,))

car1.start()
car2.start()
car3.start()
car4.start()

print("Red light")
time.sleep(1)
print("Yellow light")
time.sleep(1)
print("Green Light")
print("Go!")
semaphor.set()

#=====


#====prob2====
from facade_class import Facade

facade_obj = Facade()

print("volume of the system is {}".format(facade_obj.get_volume()))

#=====

