"""
This module describes bad examples of Python code.
You should implement a fixed version of each example.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Example 1.
strColor = "green"
boolActive = False
intPythonYears = 20
dtPythonFirstUsed = "04/20/2011"

# Example 2.
clr = "green"
ctv = False
pthnYrs = 20
pthnFrstSd = "04/20/2011"

# Example 3.
c = "green"
a = False
p = 20
t = "04/20/2011"

# Your solution should be added here.
# It should be applicable for all 3 examples.

color_name = "green"
is_true = False
use_python_years = 20
first_python_data = "04/20/2011"

# Example 4.
def do_something():pass

try:
    do_something()
except:
    pass

# Your solution should be added here.


def save_money(money):
    """
    This function can help you to calculate your saving money

    Args:    money - this is the amount you want to save;
                   should be int
    return: savings - the whole amount of savings
    """
    savings = 0
    try:
        savings += money
    except (TypeError, ValueError):
        raise Exception("Incorrect type or value of your money")
    print("You'he managed to save {}$ ".format(savings))
    return savings
