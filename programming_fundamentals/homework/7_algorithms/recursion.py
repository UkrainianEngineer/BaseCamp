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
def pow(base, power):
    if power == 0:
        return 1

    else:
        return base * pow(base, power - 1)
print(pow(5, 12))

