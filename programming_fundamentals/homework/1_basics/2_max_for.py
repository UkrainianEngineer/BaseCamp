"""
This module describes the home task related to `for` loop.
It might be useful for both students and mentors.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# This list contains your input data.
data = [1, -3, 4, 6, 11, 2, 0, -13, 9]
message = "Invalid maximum value has been found. Please check your `for` loop."

print("Your list is: {}".format(data))
maximum = 0
# Find the maximum value from `data` list using `for` loop.
# Save maximum value from `data` list into `maximum` variable.
# ADD YOUR CODE HERE.

maximum = data[0] #If all numbers are negative
for i in data:
	if i > maximum:
		maximum = i

# DON'T MODIFY THESE LINES.
assert maximum == max(data), message
print("Maximum value has been found! Congratulations!")
