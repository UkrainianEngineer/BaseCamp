"""
This module describes a very basic function in Python,
which calculates your age according to year of your birthday.
It is important to understand how to define and use functions,
because most of Python programs contains a lot of different functions.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def my_min(iterable):
    """
    DONT WRITE SUCH A CUSTOM FUNCTIONS, use builtin instead!
    Read for more details:
    https://docs.python.org/3/library/functions.html
    """
    # Get the first element of iterable.
    min_val = iterable[0]
    # Iterate through all elements of iterable except the first element.
    for value in iterable[1:]:
        # If value is less than min_val, set min_val as a value.
        if value < min_val:
            min_val = value
    return min_val

values = [-1, 4, 3, 11, -6, 2, 1, 4]
print("List of all data: {}".format(values))
print("Min value calculated by custom function: {}".format(my_min(values)))

print("Min value calculated by builtin function: {}".format(min(values)))
