from math import pi


class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def get_volume(self):
        return (4/3) * pi * (self.radius ** 3)
