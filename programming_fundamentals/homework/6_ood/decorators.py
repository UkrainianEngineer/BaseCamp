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


def decorator(original_function):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def wrapper_function(*args, **kwargs):

        for tries in range(RETRIES):
            try:
                original_function(*args, **kwargs)
                print('Function was successfully executed.')
                break
            except ValueError as err:
                print('Error occurred when attempting to run \'{}\': {}; attempt {} of {}.'
                      .format(original_function.__name__, err, (tries+1), RETRIES))

    return wrapper_function


@decorator
def my_func(number):
    # You should add some behaviour here for easier testing.
    if int(number) % 2 == 0:
        return '{} is an even number.'.format(number)
    else:
        return '{} is an odd number'.format(number)


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries=None):
    # You should add some behaviour here for easier testing.
    def real_decorator(original_function):
        def wrapper_function(*args, **kwargs):
            for tries in range(retries):
                try:
                    original_function(*args, **kwargs)
                    print('Function was successfully executed.')
                    break
                except ValueError as err:
                    print('Error occurred when attempting to run \'{}\': {}; attempt {} of {}.'
                          .format(original_function.__name__, err, (tries+1), retries))
        return wrapper_function
    return real_decorator


@decorator(retries=4)
def my_func(number):
    # You should add some behaviour here for easier testing.
    if int(number) % 2 == 0:
        return '{} is an even number.'.format(number)
    else:
        return '{} is an odd number.'.format(number)


#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#


def cached(original_function):
    cache = {}

    def wrapper_function(*args):
        if args in cache:
            print('Using data from cache. => {}'.format(cache.get(args)))
        else:
            cache[args] = original_function(*args)
            print('Calculated value. => {}'.format(cache.get(args)))
    return wrapper_function


@cached
def my_func():
    # Doing something.
    # E.g.:
    return "Hello, world!"


my_func()  # prints `Calculated value. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
my_func()  # prints `Using data from cache. => Hello, world!`
