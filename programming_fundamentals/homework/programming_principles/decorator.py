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

import datetime


def custom_decorator(some_function):

    def wrapper():
        start_time = datetime.datetime.now()
        some_function()
        end_time = datetime.datetime.now()
        time_of_execution = str(end_time - start_time)

        return 'This function executes {}.'.format(time_of_execution)

    return wrapper


@custom_decorator
def test_decorator():
    print("This function executes...")


test_decorator()
test_decorator()
