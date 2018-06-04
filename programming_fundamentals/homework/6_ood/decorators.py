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


def decorator(some_func):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.

    def func_retry():
        retry_count = 0
        while retry_count < RETRIES:
            try:
                return some_func()
            except Exception:
                retry_count = retry_count + 1
    return func_retry


@decorator
def my_func():
    # initial_param si a random number.
    # The run is successful if initial_param is < 0.5
    initial_param = random.random()
    if initial_param < 0.5:
        print("Successful run")
    else:
        print ("Run failed")
        raise Exception("Failed run")
    return initial_param

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:

def decorator_with_param(retries):
    # You should add some behaviour here for easier testing.
    def decorator_func(some_func):

        def func_retry():
            retry_count = 0
            while retry_count < retries:
                try:
                    return some_func()
                except Exception:
                    retry_count = retry_count + 1

        return func_retry
    return  decorator_func


@decorator_with_param(retries=4)
def my_func_with_param():
    # You should add some behaviour here for easier testing.
    # initial_param si a random number.
    # The run is successful if initial_param is < 0.5
    initial_param = random.random()
    if initial_param < 0.5:
        print("Successful run")
    else:
        print("Run failed")
        raise Exception("Failed run")
    return initial_param
#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#
def cached(some_func):
    cache = {}
    def cache_func(*args):
        if args in cache:
            return print("Printing value from cache -> {}".format(cache[args]))
        else:
            cache[args] = some_func(*args)
            return print("Calculating new value -> {}".format(some_func(*args)))
    return cache_func

@cached
def my_func_cached():
    return "Hello, world!"

my_func()
my_func_with_param()
my_func_cached()
my_func_cached()
my_func_cached()
my_func_cached()