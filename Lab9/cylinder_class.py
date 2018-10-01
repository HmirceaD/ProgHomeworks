from math import pi


class Cylinder:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return self.height * pi * (self.radius ** 2)
