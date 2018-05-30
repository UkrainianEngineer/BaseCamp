import datetime


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

def custom_decorator(function):
    def func_wrapper():
        start_time = datetime.datetime.now()
        function()
        end_time = datetime.datetime.now()
        diff_time = end_time - start_time
        print("This function executes {}".format(str(diff_time)))
    return func_wrapper


@custom_decorator
def test_decorator():
    print("This function executes...")


test_decorator()
test_decorator()
