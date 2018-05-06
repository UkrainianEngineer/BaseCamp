"""
This module describes a very basic example with a `while` loop in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# Example.
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
print("Original list of brands looks like this: {}".format(computer_brands))
i = 0
print("Iterating through brands one-by-one...")
while i < len(computer_brands):
    print(computer_brands[i])
    i = i + 1
