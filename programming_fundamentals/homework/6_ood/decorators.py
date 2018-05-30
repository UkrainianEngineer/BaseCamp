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


def decorator(func):
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.
    def retry_if_fails(*args, **kwargs):
        for attempt in range(RETRIES):
            try:
                func(*args, **kwargs)
                print('Function executed successfully.')
                return None  # If function executed successfully, no need to continue func execution
            except ValueError:
                print('Got exception in function trying to retry... Attempt {}'.format(attempt+1))
        print('Function execution failed on all attempts.')
    return retry_if_fails


@decorator
def my_func(number):
    # You should add some behaviour here for easier testing.
    if number == 5:
        return 5
    else:
        raise ValueError()

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:

# I use keyword-only arg retries.
def decorator(*args, retries, **kwargs):
    def real_decorator(func):
        def retry_if_fails(*args, **kwargs):
            for attempt in range(retries):
                try:
                    func(*args, **kwargs)
                    print('Function executed successfully.')
                    return None  # If function executed successfully, no need to continue func execution
                except ValueError:
                    print('Got exception in function trying to retry... Attempt {}'.format(attempt+1))
            print('Function execution failed on all attempts.')
        return retry_if_fails
    return real_decorator


@decorator(retries=4)
def my_func(number):
    # You should add some behaviour here for easier testing.
    if number == 5:
        return 5
    else:
        raise ValueError()

#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#

def cached(func):
    cache = {}
    def cache_wrapper(*args, **kwargs):
        arguments = (*args, tuple(kwargs.items()))
        if arguments in cache:
            print('Using data from cache. => {}'.format(cache[arguments]))
        else:
            function_return = func(*args, **kwargs)
            cache[arguments] = function_return
            print('Calculated value. => {}'.format(function_return))
    return cache_wrapper

@cached
def my_func():
    # Doing something.
    # E.g.:
    return "Hello, world!"

my_func() # prints `Calculated value. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
my_func() # prints `Using data from cache. => Hello, world!`
