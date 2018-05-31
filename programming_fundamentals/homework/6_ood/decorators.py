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


def decorator(target_function):
    def wrapper(*args):
        for i in range(RETRIES):
            try:
                value = target_function(*args)
                print("Success\n")
                return value
            except:
                print("Failure " + str(i+1))
        print("Failure\n")
    return wrapper


@decorator
def my_func(s=""):
    # You should add some behaviour here for easier testing.
    if random.random() < 0.75:
        raise RuntimeError("Message failed")
    print("Message: " + s)


my_func("hello")
my_func("hello")
my_func("hello")
my_func("hello")

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries):
    def inner_decorator(target_function):
        def wrapper(*args):
            for i in range(retries):
                try:
                    value = target_function(*args)
                    print("Success\n")
                    return value
                except:
                    print("Failure " + str(i+1))
            print("Failure\n")
        return wrapper
    return inner_decorator


@decorator(retries=4)
def my_func(s=""):
    # You should add some behaviour here for easier testing.
    if random.random() < 0.75:
        raise RuntimeError("Message failed")
    print("Message: " + s)


my_func("hello")
my_func("hello")
my_func("hello")
my_func("hello")

#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#


def cached(target_function):
    cache_value = None

    def wrapper():
        nonlocal cache_value
        if cache_value is None:
            cache_value = target_function()
            print("Calculated value. => " + str(cache_value))
        else:
            print("Using data from cache. => " + str(cache_value))
        return cache_value

    return wrapper


@cached
def my_func():
    # Doing something.
    # E.g.:
    return "Hello, world!"


my_func()  # prints `Calculated value. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
