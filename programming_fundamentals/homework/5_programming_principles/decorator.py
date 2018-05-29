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

import time

def custom_decorator(fn):
    # ADD YOUR CODE HERE.
    # You are also able to add some parameters if needed.
    def custom_wrapper():
        start_executing_time = time.time()
        fn()
        print(time.time() - start_executing_time)
    return custom_wrapper


@custom_decorator
def test_decorator():
    print("This function executes...")

test_decorator()
test_decorator()