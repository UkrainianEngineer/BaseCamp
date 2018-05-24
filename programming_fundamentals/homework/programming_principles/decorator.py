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

def custom_decorator(target_function):
    # ADD YOUR CODE HERE.
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        returnvalue = target_function(*args, **kwargs)
        end = time.time()
        print(end - start)
        return returnvalue
    return wrapper

  


@custom_decorator
def test_decorator():
    print("This function executes...")

@custom_decorator
def test_decorator2():
    sum = 0
    for i in range(1000000):
        sum += i 
    return sum

@custom_decorator
def test_decorator3(min, max):
    sum = 0
    for i in range (min, max):
        sum += i
    return sum

test_decorator()
test_decorator()
test_decorator2()
test_decorator3(-5000000, 10000000)
