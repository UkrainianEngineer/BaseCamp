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
def power_function(x, y):
    #  check our values
    if isinstance(x, (int, float)) and isinstance(y, int):
        if x == 0 or x == 1 or y == 1:
            return x
        if y == 0:
            return 1
        if y > 0:
            # positive case
            if y == 2:
                return x*x
            else:
                return x * power_function(x, y-1)
        elif y < 0:
            # negative case
            return 1./power_function(x, -y)
    else:
        raise TypeError('Argument must be integer or float')


x = int(input("Enter base x: "))
y = int(input("Enter exponential value y: "))
print("Result:", pow(x, y))
