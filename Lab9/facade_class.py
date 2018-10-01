from cone_class import Cone
from cube_class import Cube
from sphere_class import Sphere
from cylinder_class import Cylinder


class Facade:

    def __init__(self):
        self.sphere_obj = Sphere(3)
        self.cube_obj = Cube(3)
        self.cylinder_obj = Cylinder(3, 7)
        self.cone_obj = Cone(3, 5)

    def get_volume(self):

        return self.sphere_obj.get_volume() + self.cube_obj.get_volume() + \
               self.cylinder_obj.get_volume() + self.cone_obj.get_volume()
