"""
This module describes basic logical operators in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

print("(-0.2 > 1.4) and (0.8 < 3.1) => {}".format((-0.2 > 1.4) and (0.8 < 3.1)))  # False
print("(7.5 == 8.9) or (9.2 != 9.1) => {}".format((7.5 == 8.9) or (9.2 != 9.1)))  # True
print("not(-5.7 <= 0.3) => {}".format(not(-5.7 <= 0.3)))  # False

