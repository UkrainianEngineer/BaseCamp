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
RETRIES = 4


def decorator(func):
    def retry_func():
        # Retries counter
        counter = RETRIES
        while counter > 0:
            try:
                return func()
            except Exception:
                counter -= 1
    return retry_func


@decorator
def my_func():
    random_number = random.random()
    print(random_number)
    if random_number < 0.5:
        print('This is failed run')
        raise Exception('Failed run')
    else:
        print("Successful run")
    return random_number

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.


def decorator_with_parameter(retries=1):
    def decorator_func(func):
        def retry_func():
            # Retries counter
            counter = retries
            while counter > 0:
                try:
                    return func()
                except Exception:
                    counter -= 1
        return retry_func
    return decorator_func


@decorator_with_parameter(retries=4)
def my_func_with_parameter():
    random_number = random.random()
    print(random_number)
    if random_number < 0.5:
        print('This is failed run')
        raise Exception('Failed run')
    else:
        print("Successful run")
    return random_number

#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`


def cached(func):
    # Creating empty cache
    cache = {}

    def caching_func(*args):
        if args in cache:
            return print('Using data from cache. => {}'.format(cache[args]))
        else:
            rv = func(*args)
            cache[args] = rv
            return print('Calculated value. => {}'.format(rv))
    return caching_func


@cached
def my_cached_func():
    return "Hello, world!"


my_func()
my_func_with_parameter()
my_cached_func()  # prints `Calculated value. => Hello, world!`
my_cached_func()  # prints `Using data from cache. => Hello, world!`
my_cached_func()  # prints `Using data from cache. => Hello, world!`
my_cached_func()  # prints `Using data from cache. => Hello, world!`
