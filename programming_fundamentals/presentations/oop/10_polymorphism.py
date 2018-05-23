"""
This module describes a basic polymorphism in Python.
"""
import math

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    figures = [Rectangle(10, 20), Circle(15), Rectangle(15, 40), Circle(20), Rectangle(50, 100)]
    for figure in figures:
        print(figure.get_area())
