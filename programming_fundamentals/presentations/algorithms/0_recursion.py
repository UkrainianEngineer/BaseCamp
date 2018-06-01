"""
This module describes a very basic example of recursion in Python's class.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def slice_pizza(number_of_friends, number_of_slices):
    # Cut pizza in half.
    number_of_slices = number_of_slices * 2

    # Is there enough slices for everybody?
    if number_of_slices >= number_of_friends:
        # If yes - return our slices, it's time to eat pizza!
        return number_of_slices
    else:
        # If not - then cut it in half once again.
        return slice_pizza(number_of_friends, number_of_slices)


print(slice_pizza(15, 1))