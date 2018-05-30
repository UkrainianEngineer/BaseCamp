"""
This module describes a homework related to decorator topic.
"""
import time

START_TIME = time.time()

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Create a decorator `custom_decorator` which calculates an execution time
# of the `test_decorator` function.
# After each execution of `test_decorator` function print execution time.
# You DONT'T NEED ANY CHANGES FOR `test_decorator` function
# or any specific executions of this function.
# JUST MODIFY `custon_decorator` decorator.

def custom_decorator(my_function):
    # ADD YOUR CODE HERE.
    # You are also able to add some parameters if needed.
    def wrapper():
        my_function()
        # Set a delay
        time.sleep(2)
        print(time.time() - START_TIME)

    return wrapper


@custom_decorator
def test_decorator():
    print("This function executes...")

test_decorator()
test_decorator()