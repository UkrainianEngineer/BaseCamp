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


def decorator(func_to_decorate):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def wrapper():
        for i in range(RETRIES):
            print("Attempt {}".format(i + 1))
            try:
                func_to_decorate()
                break
            except RuntimeError:
                print("Failure")
        print(" ")

    return wrapper


@decorator
def my_func():
    # You should add some behaviour here for easier testing.
    if random.random() < 0.6:
        raise RuntimeError("Failed by Exception")
    print("Success")

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.


def decorator(retries):
    # You should add some behaviour here for easier testing.
    def outer_decorator(func_to_decorate):
        def wrapper():
            for i in range(retries):
                print("Attempt {}".format(i + 1))
                try:
                    func_to_decorate()
                    break
                except RuntimeError:
                    print("Failure")
            print(" ")
        return wrapper
    return outer_decorator


@decorator(retries=4)
def my_func():
    # You should add some behaviour here for easier testing.
    if random.random() < 0.6:
        raise RuntimeError("Failed by Exception")
    print("Success")


#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`


def cached(target_function):

    cached_state = None

    def wrapper():
        nonlocal cached_state

        if cached_state is None:
            cached_state = target_function()
            print("Calculated value. => {}".format(cached_state))
        else:
            print("Using data from cache. => {}".format(cached_state))
        return cached_state

    return wrapper


@cached
def my_func():
    # Doing something.
    # E.g.:
    return "Hello, world!"

my_func() # prints `Calculated value. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
