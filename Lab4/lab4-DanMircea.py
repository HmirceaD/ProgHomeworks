import shapes
import sys

compute_functions = ["compute_square", "compute_rectangle", "compute_triangle"]


def compute_square():
    length = float(input("Enter the side of the square:\n"))
    print("The area of the triangle is {}"
          .format(shapes.square_area(length)))


def compute_rectangle():
    length1 = float(input("Enter the first side of the rectangle:\n"))
    length2 = float(input("Enter the second side of the rectangle:\n"))

    print("The area of the rectangle is {}"
          .format(shapes.rectangle_area(length1, length2)))


def compute_triangle():

    side1 = float(input("Enter the first side of the triangle:\n"))
    side2 = float(input("Enter the second side of the triangle:\n"))
    side3 = float(input("Enter the third side of the triangle:\n"))

    print("The area of the triangle is {}"
          .format(shapes.triangle_area(side1, side2, side3)))


def display_menu():

    my_module = sys.modules[__name__]

    try:
        answer = int(input("Enter the shape for which "
                           "you want to compute the area:"
                           "\n1.Square\n2.Rectangle\n3.Triangle"))

        if 1 <= answer <= 3:
            if hasattr(my_module, compute_functions[answer - 1]):
                getattr(my_module, compute_functions[answer - 1])()
        else:
            print("Not an option, select something else")
            sys.exit(2)

    except ValueError:
        print("Answer must be a number")
        sys.exit(1)


display_menu()
