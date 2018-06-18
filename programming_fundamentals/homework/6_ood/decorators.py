"""This module describes homework related to decorators.
   Author: pivanchy.
"""

from functools import lru_cache

# Implement `retry` decorator.
# If some part of code in decorated function fails, try to re-run it again.
# If decorated function executes successfully, you don't need to re-run it.
#
# 1) add some global variable like `RETRIES = 4`.
#    Use this variable for your retry decorator.
#    Failed function should retries up to 4 times.
#

# Example:
RETRIES = 4

def decorator(my_func):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def wrap(argnum):
        print('I try to execute it!')
        for a in range(RETRIES):
            try:
                my_func(argnum)
                print ('Execute!')
                break
                
            except:
                print ('Error! Try number... ' + str(a+1))
    return wrap

@decorator
def my_func(a):
# You should add some behaviour here for easier testing.
    a = 1 / a





# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


# Example:
RETRIES = 4
def decorator_param(ret):
    def decorator(my_func):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
        def wrap(divex):
            print('I try to execute it!')
            for a in range(ret):
                try:
                    #my_func(divex)
                    print ('Execute! Res = ' + str(my_func(divex)))
                    break
                
                except:
                    print ('Error! Try number... ' + str(a+1))
            print('End!')
        return wrap
    return decorator

@decorator_param(ret = 5)
def my_func(div):
# You should add some behaviour here for easier testing.
    a = 1 / div
    return a
    
#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#


@lru_cache()
def my_func2():
    print('Hello world!')

my_func2() # prints `Calculated value. => Hello, world!`
my_func2() # prints `Using data from cache. => Hello, world!`
my_func2() # prints `Using data from cache. => Hello, world!`
my_func2() # prints `Using data from cache. => Hello, world!`
