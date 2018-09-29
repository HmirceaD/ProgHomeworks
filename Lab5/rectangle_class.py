from shape_class import Shape


class Rectangle(Shape):

    def __init__(self, name, length1, length2):
        super(Rectangle, self).__init__(name)
        self.length1 = length1
        self.length2 = length2

    def display(self):
        print(self.name)

    def getarea(self):
        return self.length1 * self.length2
