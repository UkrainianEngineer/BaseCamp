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
    def wrapper(*args, **kwargs):
        global RETRIES

        while RETRIES:
            try:
                result = func(*args, **kwargs)
                return result
            except TypeError as exp:
                print(exp)
                RETRIES -= 1
                continue

    return wrapper


@decorator
def my_func(sequence):
    # You should add some behaviour here for easier testing.
    """
        Args:
            sequence (list) - list of words.
        Returns:
            max_len (int) - length of the longest word.
        """
    list_ = sequence.copy()
    words_length = list(map(len, list_))

    return max(words_length)

# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:


def retry_decorator(retries=1):
    # You should add some behaviour here for easier testing.
    def decorator(func):
        def wrapper(*args, **kwargs):
            count_retries = retries
            while count_retries:
                try:
                    my_func = func(*args, **kwargs)
                    return my_func
                except Exception as exp:
                    print(exp)
                    count_retries -= 1
                    continue

        return wrapper

    return decorator


@retry_decorator(retries=3)
def my_func(sequence):
    # You should add some behaviour here for easier testing.
    """
        Args:
            sequence (list) - list of words.
        Returns:
            max_len (int) - length of the longest word.
        """
    list_ = sequence.copy()
    words_length = list(map(len, list_))

    return max(words_length)

#  3) Implement decorator which caches data.
#     It means that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:


def cached(func):
    cache = []

    def decorator(*args, **kwargs):
        nonlocal cache
        result = func(*args, **kwargs)

        if id(func) not in cache:
            cache.append(id(func))
            return '{} => {}'.format('Calculated value.', result)
        else:
            return '{} => {}'.format('Using data from cache.', result)
    return decorator


@cached
def my_func():
    return "Hello, world!"


print(my_func()) # prints `Calculated value. => Hello, world!`
print(my_func()) # prints `Using data from cache. => Hello, world!`
print(my_func()) # prints `Using data from cache. => Hello, world!`
print(my_func()) # prints `Using data from cache. => Hello, world!`
