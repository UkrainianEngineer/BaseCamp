"""
This module describes a simple exception handling in Python.
It is important to understand how to work with exceptions in Python.
We're able to handle these errors same as raise if needed.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# Handling a `ZeroDivisionError`.
try:
    print(1/0)
except ZeroDivisionError:
    print("Handled ZeroDivisionError!")
print("Successfully finished!")
