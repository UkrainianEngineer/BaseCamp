"""This module describes homework related to decorators.
   Author: pivanchy.
"""

from random import randint

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
    def wrapper():
        attempt = RETRIES
        while attempt > 0:
            try:
                return func()
                break
            except Exception as errors:
                print('Error: ', errors)
                attempt -= 1
    return wrapper
                

@decorator
def guess_number():
    # You should add some behaviour here for easier testing.
    number = int(input('Enter number fro 0 to 9:'))
    rand_number = randint(0, 9)
    if number == rand_number:
        print('You Win!')
    else:
        print('You Loose!')

guess_number()   


# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries):
    # You should add some behaviour here for easier testing.
    def inner_decorator(func):
        def wrapper():
            attempt = retries
            while attempt > 0:
                try:
                    return func()
                except Exception as errors:
                    print('Error: ', errors)
                    attempt -= 1
        return wrapper
    return inner_decorator


@decorator(retries=4)
def favorite_number():
    # You should add some behaviour here for easier testing.
    number = int(input('Enter your favorite number:'))
    print('Your favorite number is: ', number)

favorite_number()

    
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
    cached_value = {}
    def wrapper(*args):
        if args in cached_value:
            print('Using data from cache. =>', cached_value[args])
        else:
            returned_value = func(*args)
            cached_value[args] = returned_value
            print('Calculated value. =>', returned_value)
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
