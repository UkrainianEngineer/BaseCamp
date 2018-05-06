"""
This module describes a very basic function in Python,
which calculates your age according to year of your birthday.
It is important to understand how to define and use functions,
because most of Python programs contains a lot of different functions.
"""
import datetime

YEAR_OF_BIRTH = 1990

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def years(year_of_birth):
    """Calculate current age according to year of birthday."""
    now = datetime.datetime.now()
    return now.year - year_of_birth

my_years = years(YEAR_OF_BIRTH)

print("You're {} years old." .format(my_years))

