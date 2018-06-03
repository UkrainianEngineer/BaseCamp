"""This module describes homework related to decorators.
   Author: pivanchy.
"""

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


def decorator(fn):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def wrapper_fn(arg):
        for i in range(RETRIES):
            try:
                fn(arg)
                print("Function succeed")
                break
            except ZeroDivisionError:
                print("Function is failed. Attempt " + str(i + 1))
                continue

    return wrapper_fn


@decorator
def my_func(number):
    # You should add some behaviour here for easier testing.
    if number > 0:
        return 5 / number
    else:
        raise ZeroDivisionError


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries):
    # You should add some behaviour here for easier testing.
    def real_decorator(fn):
        def wrapper_fn(arg):
            for i in range(retries):
                try:
                    fn(arg)
                    print("Function succeed")
                    break
                except ZeroDivisionError:
                    print("Function is failed. Attempt " + str(i + 1))
                    continue

        return wrapper_fn

    return real_decorator


@decorator(retries=4)
def my_func(number):
    # You should add some behaviour here for easier testing.
    if number > 0:
        return 5 / number
    else:
        raise ZeroDivisionError


#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#

def cached(fn):
    data = None

    def wrapper():
        nonlocal data
        if fn() is data:
            print("Using data from cache. => " + data)
        else:
            print("Calculated value. => " + fn())
            data = fn()
        return data
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
