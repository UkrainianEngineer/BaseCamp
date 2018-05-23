"""
This module describes a very basic example how to check variable type in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if type(numbers) == list:
    # This is a bad example.
    print("List type.")

if isinstance(numbers, list):
    # This is a good example.
    print("List type.")

