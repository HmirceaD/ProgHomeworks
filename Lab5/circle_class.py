from shape_class import Shape
from math import pi


class Circle(Shape):

    def __init__(self, name, radius):
        super(Circle, self).__init__(name)
        self.radius = radius

    def display(self):
        print(self.name)

    def getarea(self):
        return pi * (self.radius ** 2)
