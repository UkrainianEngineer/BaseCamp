"""This module describes homework related to decorators.
   Author: pivanchy.
"""

from programming_fundamentals.homework.coffee_preparation import Coffee

# Implement `retry` decorator.
# If some part of code in decorated function fails, try to re-run it again.
# If decorated function executes successfully, you don't need to re-run it.
#
# 1) add some global variable like `RETRIES = 4`.
#    Use this variable for your retry decorator.
#    Failed function should retries up to 4 times.

RETRIES = 4


def decorator(func):
    def retry(*a, **k):
        count = 0
        while count < RETRIES:
            try:
                func(*a, **k)
                print("I'd do coffee!")
                return True
            except (ValueError, TypeError):
                print("Function failed = " + str(count+1) + "times")
                count += 1
        else:
            raise Exception(mssg="Function failed all times")
    return retry


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
@decorator
def my_func(value):
    if value > 0:
        brewer = Coffee()
        brewer.install_filter()
        brewer.add_spoons(value)
        brewer.turn_on()
        brewer.brew()
    else:
        raise ValueError


def decorator(retries):
    def func_decorator(func):
        def retry(*a, **k):
            count = 0
            while count < retries:
                try:
                    func(*a, **k)
                    print("I'd do coffee!")
                    return True
                except ValueError:
                    print("Function failed = " + str(count+1) + "times")
                    count += 1
            else:
                raise Exception(mssg="Function failed all times")
        return retry
    return func_decorator


@decorator(retries=4)
def my_func(value):
    if value > 0:
        brewer = Coffee()
        brewer.install_filter()
        brewer.add_spoons(value)
        brewer.turn_on()
        brewer.brew()
    else:
        raise ValueError


#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`

def cached(func, value=None):

    def cache_wrapper():
        nonlocal value
        if value is None:
            value = func()
            print("Calculated value. => " + str(value))
        else:
            print("Using data from cache. => " + str(value))
        return value

    return cache_wrapper


@cached
def my_func():
    return "Hello, world!"


my_func()  # prints `Calculated value. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
