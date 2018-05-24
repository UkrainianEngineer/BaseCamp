"""
This module describes a homework related to decorator topic.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

import time

# Create a decorator `custom_decorator` which calculates an execution time
# of the `test_decorator` function.
# After each execution of `test_decorator` function print execution time.
# You DONT'T NEED ANY CHANGES FOR `test_decorator` function
# or any specific executions of this function.
# JUST MODIFY `custon_decorator` decorator.

# waiting time to prolong testing function execution
wait_time = 1.5


def custom_decorator(func):
    def execution_time():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return execution_time


@custom_decorator
def test_decorator():
    print("This function executes...")
    time.sleep(wait_time)


test_decorator()
test_decorator()
