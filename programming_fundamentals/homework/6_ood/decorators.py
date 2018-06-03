"""This module describes homework related to decorators.
   Author: pivanchy.
"""
import random

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


def decorator(func):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def wrapper(*args, **kwargs):
        count = 0
        try:
            func(*args, **kwargs)
            print('Function was successfully executed.')
        except (ValueError, TypeError):
            print("Function failed = " + str(count + 1) + "times")
            count += 1
    return wrapper




@decorator
def my_func():
    # You should add some behaviour here for easier testing.
    random_number = random.random()
    if random_number < 0.8:
        raise Exception('Failed run')
    else:
        print("Success")
    return random_number

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries=None):
    # You should add some behaviour here for easier testing.
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            while count > retries:
                try:
                    return func()
                except Exception:
                    count += 1
        return wrapper
    return func_decorator


@decorator(retries=4)
def my_func():
    # You should add some behaviour here for easier testing.
    random_number = random.random()
    if random.random() < 0.8:
        raise Exception('Failed run')
    else:
        print("Success")
    return random_number

#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#


def cached(func):
    cache = []

    def decorator(*args, **kwargs):
        nonlocal cache
        result = func(*args, **kwargs)

        if id(func) not in cache:
            cache.append(id(func))
            return '{} => {}'.format('Calculated value.', result)
        else:
            return '{} => {}'.format('Using data from cache.', result)
    return decorator

@cached
def my_cached_func():
    return "Hello, world!"

my_func() # prints `Calculated value. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
