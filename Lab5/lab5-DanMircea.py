import circle_class
import rectangle_class
import square_class
import triangle_class
import sys

compute_functions = ["compute_square", "compute_rectangle", "compute_triangle", "compute_circle"]


def compute_square():
    length = float(input("Enter the side of the square:\n"))

    square_obj = square_class.Square("square", length)

    print("The area of the triangle is {}"
          .format(square_obj.getarea()))


def compute_rectangle():
    length1 = float(input("Enter the first side of the rectangle:\n"))
    length2 = float(input("Enter the second side of the rectangle:\n"))

    rectangle_obj = rectangle_class.Rectangle("rectangle", length1, length2)

    print("The area of the rectangle is {}"
          .format(rectangle_obj.getarea()))


def compute_triangle():

    side1 = float(input("Enter the first side of the triangle:\n"))
    side2 = float(input("Enter the second side of the triangle:\n"))
    side3 = float(input("Enter the third side of the triangle:\n"))

    triangle_obj = triangle_class.Triangle("Azorel", side1, side2, side3)

    print("The area of the triangle is {}"
          .format(triangle_obj.getarea()))


def compute_circle():

    radius = float(input("Give the circle radius\n"))

    circle_obj = circle_class.Circle("circle", radius)

    print("The area of the triangle is {}"
          .format(circle_obj.getarea()))


def display_menu():

    my_module = sys.modules[__name__]

    try:
        answer = int(input("Enter the shape for which "
                           "you want to compute the area:"
                           "\n1.Square\n2.Rectangle"
                           "\n3.Triangle\n4.Circle"))

        if 1 <= answer <= 4:
            if hasattr(my_module, compute_functions[answer - 1]):
                getattr(my_module, compute_functions[answer - 1])()
        else:
            print("Not an option, select something else")
            sys.exit(2)

    except ValueError:
        print("Answer must be a number")
        sys.exit(1)


display_menu()
