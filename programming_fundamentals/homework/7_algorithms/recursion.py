"""
This module describes a homework related to recursive functions.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Create a recursive power function.
# This function should calculate x ** y using recursion.
# It might be calculated using formula:
# x ** y == x * x ** (y - 1).
# Example:
# 2 ** 5 == 2 * 2 ** 4 == 2 * 2 * 2 ** 3 == ... = 2 * 2 * 2 * 2 * 2
# Note:
# x ** 0 == 1.
#
# Example of function usage:
# pow(2, 3)  # Returns 8.
# pow(4, 6)  # Returns 4096.
# And so on.

def power(x, y):
    """
    Args:
        x (int) - the base
        y (int) - the exponent
    Returns:
        int - x to the power of y
    """
    if y == 0:
        return 1
    elif y < 0:
        return 1 / (x * power(x, abs(y)-1))
    else:
        return x * power(x, y-1)