"""
This module describes simple example with `continue` in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# Example.
print("Iteration over loop [0, 10] with a `continue` condition, if the number is equal to 3.")
for i in range(10):
    if i == 3:
        continue
    print(i)
