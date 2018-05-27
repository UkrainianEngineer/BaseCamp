"""
This module describes a homework related to decorator topic.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"
import datetime

# Create a decorator `custom_decorator` which calculates an execution time
# of the `test_decorator` function.
# After each execution of `test_decorator` function print execution time.
# You DONT'T NEED ANY CHANGES FOR `test_decorator` function
# or any specific executions of this function.
# JUST MODIFY `custon_decorator` decorator.

def custom_decorator(some_func):
    # ADD YOUR CODE HERE.
    # You are also able to add some parameters if needed.
    def wrapper_func(*args, **kwargs):
        start = datetime.datetime.now()
        some_func()
        stop = datetime.datetime.now()
        diff = stop - start
        print (diff)
    return wrapper_func



@custom_decorator
def test_decorator():
    print("This function executes...")

test_decorator = custom_decorator(test_decorator)
test_decorator()
test_decorator()