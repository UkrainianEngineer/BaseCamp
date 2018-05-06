"""
This module describes a very basic examples with the `for` loop.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# First example.
print("This is the first example.")
print("=" * 60)
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
print("Original list of brands looks like: {}".format(computer_brands))
print("Iterating through brands one-by-one...")
for brand in computer_brands:
    print(brand)
print("=" * 60)

# Second example.
print("This is the second example.")
numbers = [1,10,20,30,40,50]
print("Original list of numbers looks like: {}".format(numbers))
summ = 0
print("Iterating through numbers one-by-one...")
for number in numbers:
    summ = summ + number
    print(summ)
print("=" * 60)
