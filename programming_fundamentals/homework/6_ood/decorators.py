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
    def wrapper(*args, **kwargs):
	try:
	    print(func(*args, **kwargs))
	except IndexError as e:
	    print(e)
	    print("Function will be rerun {} times.".format(RETRIES))
	    for i in range(RETRIES):
		try:
		    print("Calculation result is {}".format(func(*args, **kwargs)))
		except IndexError as e:
		    print("IndexError raised at rerun #{}".format(i+1))
		    continue
    return wrapper
    # Use `RETRIES` variable here somehow.
    # You should add some behaviour here for easier testing.


@decorator
def my_func(index):
    return ['spring', 'summer', 'autumn', 'winter'][index]
    # You should add some behaviour here for easier testing.

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def decorator(retries, **retry_number):
    def real_decorator(func):
	def wrapper(*args, **kwargs):
	    try:
		print(func(*args, **kwargs))
	    except IndexError as e:
		print(e)
		print("Function will be rerun {} times.".format(retries))
		for i in range(retries):
		    try:
			print("Calculation result is {}".format(func(*args, **kwargs)))
		    except IndexError as e:
			print("IndexError raised at rerun #{}".format(i+1))
			continue
	return wrapper
    return real_decorator
    # You should add some behaviour here for easier testing.


@decorator(retries=4)
def my_func(index):
    return ['spring', 'summer', 'autumn', 'winter'][index]
#
#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#
def cached(function):
    cached_data = {}
    def wrapper(*args):
        if args in cached_data:
            print("Using data from cache. => {}".format(cached_data[args]))
        else:
            new_value = function(*args)
            cached_data[args] = new_value
            print("Calculated value. => {}".format(new_value))
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
