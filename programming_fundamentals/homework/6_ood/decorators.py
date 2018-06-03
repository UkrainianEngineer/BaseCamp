"""This module describes homework related to decorators.
   Author: pivanchy.
"""

import datetime

# Implement `retry` decorator.
# If some part of code in decorated function fails, try to re-run it again.
# If decorated function executes successfully, you don't need to re-run it.
#
# 1) add some global variable like `RETRIES = 4`.
#    Use this variable for your retry decorator.
#    Failed function should retries up to 4 times.

# Example:
RETRIES = 4


def decorator(test_function):

    def wrapper():
        retries_num = RETRIES

        while retries_num > 0:
            retries_num -= 1
            try:
                return test_function()
            except Exception as e:
                print(e)
        print('All {} retries failed.'.format(RETRIES))

    return wrapper


@decorator
def my_func():
    some_time = datetime.datetime.now()
    if some_time.microsecond % 2 == 0:
        raise Exception('Fail!')
    else:
        print('Success!')


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.


def decorator(retries):
    def real_decorator(test_function):
        def wrapper():

            retries_num = retries

            while retries_num > 0:
                retries_num -= 1
                try:
                    return test_function()
                except Exception as e:
                    print(e)
            print('All {} retries failed.'.format(retries))

        return wrapper
    return real_decorator


@decorator(retries=2)
def my_func():
    some_time = datetime.datetime.now()
    if some_time.microsecond % 2 == 0:
        raise Exception('Fail!')
    else:
        print('Success!')


#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`

def cached(test_function):
    cash_value = None

    def wrapper():
        nonlocal cash_value

        if cash_value is None:
            cash_value = test_function()
            print('Calculated value. => {}'.format(cash_value))
        else:
            print('Using data from cache. => {}'.format(cash_value))

    return wrapper


@cached
def my_func():
    return "Hello, world!"


my_func()  # prints `Calculated value. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
