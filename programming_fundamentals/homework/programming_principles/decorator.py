"""
This module describes a homework related to decorator topic.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Create a decorator `custom_decorator` which calculates an execution time
# of the `test_decorator` function.
# After each execution of `test_decorator` function print execution time.
# You DONT'T NEED ANY CHANGES FOR `test_decorator` function
# or any specific executions of this function.
# JUST MODIFY `custon_decorator` decorator.

def custom_decorator(executed_func):
    # ADD YOUR CODE HERE.
    # You are also able to add some parameters if needed.
    def calculate_time(*args, **kwargs):
	import datetime
	start = datetime.datetime.now()
	func_time = executed_func(*args, **kwargs)
	end = datetime.datetime.now()
	print("Execution time equals {}".format(end-start))
        return func_time
    return calculate_time


@custom_decorator
def test_decorator():
    print("This function executes...")

test_decorator()
test_decorator()
