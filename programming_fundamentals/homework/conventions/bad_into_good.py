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
color = "green"
is_active = False
python_age =20
first_usage_date = "04/20/2011"
# It should be applicable for all 3 examples.


# Example 4.
def do_something():pass

try:
    do_something()
except:
    pass

# Your solution should be added here.


def handle_exceptions(test_number):
    # This function uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # It handles possible exceptions.

    while True:
        try:
            user_number = int(input("Please enter your number: "))
            if user_number > test_number:
                print('Yey! My number is higher!')
            elif user_number < test_number:
                print('Wow! My number is lower!')
            break
        except ValueError:
            print("You didn't entered the number.")


