"""
This module describes a basic difference between `is` and `==` operators in Python.
"""
from utils import prepare_output

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# These examples show a basic difference between `is` and `==` operators.
print(prepare_output("4 == 4", 4 == 4))
print(prepare_output("4 is 4", 4 is 4))
print(prepare_output("[1, 2] == [1, 2]", [1, 2] == [1, 2]))
print(prepare_output("[1, 2] is [1, 2]", [1, 2] is [1, 2]))