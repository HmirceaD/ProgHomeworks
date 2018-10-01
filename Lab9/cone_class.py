from math import pi


class Cone:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return (1/3) * pi * (self.radius ** 2) * self.height
