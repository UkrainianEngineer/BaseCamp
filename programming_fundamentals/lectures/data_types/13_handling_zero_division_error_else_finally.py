"""
This module describes a simple exception handling in Python.
It is important to understand how to work with exceptions in Python.
We're able to handle these errors same as raise if needed.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# Handling a `ZeroDivisionError` with an additional conditions.
try:
    print("Try")
except:
    print("Exception")
else:
    print("Else")
finally:
    print("Finally")
print("Successfully finished!")
