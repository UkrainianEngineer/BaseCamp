"""
This module describes a homework related to decorator topic.
"""

import time

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Create a decorator `custom_decorator` which calculates an execution time
# of the `test_decorator` function.
# After each execution of `test_decorator` function print execution time.
# You DONT'T NEED ANY CHANGES FOR `test_decorator` function
# or any specific executions of this function.
# JUST MODIFY `custom_decorator` decorator.

#func decorator
def custom_decorator(func):
    #decorator
    def decor_wrap():
    # ADD YOUR CODE HERE.
        #func for decorate
        #code before
        begin_time = time.time()
        func()
        end_time = time.time()
        print(str(end_time - begin_time))
        #code after
    return decor_wrap

@custom_decorator
def test_decorator():
    print("This function executes...")

test_decorator()
test_decorator()
