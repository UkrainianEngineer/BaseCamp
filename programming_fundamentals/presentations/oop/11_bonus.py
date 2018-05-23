"""
This module describes a basic polymorphism in Python.
"""
import math

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Test:
    __private_var = 42


if __name__ == '__main__':
    test = Test()
    # This raises an error.
    print(test.__private_var)
    # It works.
    print(test._Test__private_var)

