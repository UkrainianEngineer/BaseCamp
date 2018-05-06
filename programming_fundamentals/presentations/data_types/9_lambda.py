"""
This module describes a simple lambda functions.
It is important to understand how to define and use lambda functions.
The most important thing is: DON'T SAVE LAMBDA FUNCTIONS AS A VARIABLE!!!
Just use a simple functions in this case.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# This is a wrong usage of lambda functions.
# We don't expect to save lambda function as a variable.
double = lambda x: x*2
print("Called lambda assigned to variable: {}".format(double(5)))
print("Inline lambda function call: {}".format((lambda x: x*2)(5)))
