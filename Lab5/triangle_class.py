from shape_class import Shape
from math import sqrt


class Triangle(Shape):

    def __init__(self, name, side1, side2, side3):
        super(Triangle, self).__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def display(self):
        print(self.name)

    def getarea(self):
        semiper = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(semiper * (semiper - self.side1)*(semiper - self.side2)*(semiper - self.side3))
