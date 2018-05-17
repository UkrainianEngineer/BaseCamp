"""
This module describes the hometask related to `while` loop.
It might be useful for both students and mentors.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

NUMBER_OF_STEPS = 10
message = "There were not enough of iteration. Please check your `while` loop."

step_count = 0
# Iterate `NUMBER_OF_STEPS` times using `while` loop.
# Increase `step_count` variable by 1 in each loop.
# `step_count` should contains number of iterations.
# ADD YOUR CODE HERE.

while step_count < NUMBER_OF_STEPS:
    step_count += 1

# DON'T MODIFY THESE LINES.
print("Iterated {} times.".format(step_count))
assert step_count == NUMBER_OF_STEPS, message

