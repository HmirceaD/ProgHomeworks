from shape_class import Shape


class Square(Shape):

    def __init__(self, name, length):
        super(Square, self).__init__(name)
        self.length = length

    def display(self):
        print(self.name)

    def getarea(self):
        return self.length ** 2