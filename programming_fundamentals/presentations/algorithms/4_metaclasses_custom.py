"""
This module describes a very basic example of custom metaclass creation in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Meta(type):
    pass


class Complex(metaclass=Meta):
    pass


class Custom:
    # This class is equalent to previous.
    __metaclass__ = Meta

print(type(Complex))
