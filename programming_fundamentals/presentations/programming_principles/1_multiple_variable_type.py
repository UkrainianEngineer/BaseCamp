"""
This module describes a very basic example how to check variable type in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if type(numbers) == list or type(numbers) == tuple:
    # This is a bad example.
    print("List or tuple type.")

if isinstance(numbers, list) or isinstance(numbers, tuple):
    # This is a bad example.
    print("List or tuple type.")

if isinstance(numbers, (list, tuple)):
    # This is a good example.
    print("List or tuple type.")


