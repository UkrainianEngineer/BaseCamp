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
color = "green"
active = False
python_years = 20
python_first_used = "04/20/2011"


# Your solution should be added here.
def divisible_by_2(value):
    if value < 0:
        raise ValueError
    if value % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
try:
    num = int(input("Enter your number: "))
    divisible_by_2(num)
except ValueError:
    print ("Only positive integers are allowed")



