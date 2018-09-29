from math import sqrt


def square_area(length):
    return length*length


def rectangle_area(length1, length2):
    return length1*length2


def triangle_semiperimeter(side1, side2, side3):
    return (side1 + side2 + side3) / 2


def triangle_area(side1, side2, side3):
    s = triangle_semiperimeter(side1, side2, side3)
    return sqrt(s * (s - side1)*(s - side2)*(s-side3))
