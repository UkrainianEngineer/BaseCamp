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

        for i in range(RETRIES):
            try:
                result = func(*args, **kwargs)
            except TypeError as exp:
                print(exp)
                continue
            return result
    return wrapper


@decorator
def longest_word(sequence):
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
            nonlocal retries
            for i in range(retries):
                try:
                    result = func(*args, **kwargs)
                except Exception as exp:
                    print(exp)
                    continue
                return result
        return wrapper
    return decorator


@retry_decorator(retries=2)
def longest_word(sequence):
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
    cache = {}

    def decorator(*args, **kwargs):
        nonlocal cache
        result = func(*args, **kwargs)
        arguments = args, tuple(kwargs.items())
        info = func, arguments

        if info in cache:
            print('Using data from cache.', end=' => ')
            result = cache[info]
        else:
            cache[info] = result
            print('Calculated value.', end=' => ')

        return result
    return decorator


@cached
def arg_sum(*args, **kwargs):
    args_sum = sum(args) + sum(kwargs.values())

    return args_sum


def main():
    print('Task 2:')
    print(longest_word(['yosemite', 'yellowstone', 'sequoia', 11]))

    print('-' * 25)

    print('Task 3:')
    print(arg_sum(1, 7, c=5))
    print(arg_sum(3, 5, d=4))
    print(arg_sum(1, 7, c=5))
    print(arg_sum(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()


