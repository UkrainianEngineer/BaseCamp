"""This module describes homework related to decorators.
   Author: pivanchy.
"""
import datetime

RETRIES = 4
count = 0

# Implement `retry` decorator.
# If some part of code in decorated function fails, try to re-run it again.
# If decorated function executes successfully, you don't need to re-run it.
#
# 1) add some global variable like `RETRIES = 4`.
#    Use this variable for your retry decorator.
#    Failed function should retries up to 4 times.
#
# Example:


def decorator(function):

    def func_wrapper(*agrs, **kwargs):
        global count
        start_time = datetime.datetime.now()
        try:
            function(*agrs, **kwargs)
        except (TypeError or ValueError):
            count += 1
            if count < RETRIES:
                return func_wrapper()
        end_time = datetime.datetime.now()
        print("This function executes {}".format(str(end_time - start_time)))

    return func_wrapper


@decorator
def my_func():
    print("This function executes..." + 1)


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            for _ in range(retries):
                try:
                    func_value = function(*args, **kwargs)
                    return func_value
                except (NameError, TypeError or ValueError):
                    print("An error occured during function execution")
            end_time = datetime.datetime.now()
            print("This function executes {}".format(str(end_time - start_time)))
        return wrapper
    return real_decorator


@decorator(retries=4)
def my_func(n):
    summ = 0
    for i in range(n):
        summ += i
    print("Summ is equal: " + summ1)
    return summ

    print(my_func(77))

#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:


# version 1
def cached(function):

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        value = function(*args, **kwargs)
        if wrapper.calls > 1:
            print("Using data from cache. => {}".format(str(value)))
        else:
            print("Calculated value. => {}".format(str(value)))
        return function(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


# version 2
def cached(function):
    cache = {}

    def wrapper(*args, **kwargs):
        nonlocal cache
        value = (*args, tuple(kwargs.items()))
        if value not in cache:
            return_value = function(*args, **kwargs)
            cache[value] = return_value
            print('Calculated value. => {}'.format(return_value))
        else:
            print('Using data from cache. => {}'.format(cache[value]))
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
