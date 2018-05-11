"""
This module describes the hometask related to `slicing` loop.
It might be useful for both students and mentors.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

data = [3, 11, 2, -6, 8, 17, 3]
message = "Invalid sum has been found. Check your sum again."
N = 2
M = 3


print("Input data is: {}".format(data))
summ = 0
# Calculate sum of elements from list from `N` element to `M` using slicing.
# Use builtin `sum` function for finding sum.
# Store sum of elements from `N` to `M` into `summ` variable.
# Example:
# data = [1,2,3,4,5]
# N = 2
# M = 5
# summ = data[2] + data[3] + data[4]
# summ = 3 + 4 + 5 = 12

# ADD YOUR CODE HERE.

summ = sum(data[N:M])

# DON'T MODIFY THESE LINES.
expected = 0
for i in range(N, M):
    expected += i
assert summ == expected, message
print("Congratulations! You've done this task!")
