#!/usr/bin/env python
"""
This module contains tasks related to data types in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

TEST_NUMBER = 42


def decimal_to_binary(n):
    """
    This function converts decimal(integer) into binary.
    Args: n (int) - integer number to convert.
    Returns: int - integer number of binary representation for enterd n.
    """
    binary_values = []

    while n > 0:
        binary_values.append(str(n % 2))
        n = n // 2

    binary_values.reverse()
    binary_final = ''.join(binary_values)
    return int(binary_final)


def binary_to_decimal(n):
    """
    This function converts binary into integer(decimal).
    Args: n (int) - binary representation of a number.
    Returns: int - decimal representation of a proper number.
    """
    binary_value = str(n)
    exponent = len(binary_value) - 1
    decimal_values = []

    for i in binary_value:
        decimal_values.append(int(i) * (2 ** exponent))
        exponent -= 1

    return sum(decimal_values)


def storage(data_for_storage=None, *args, **kwargs):
    # This function returns list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.

    data_storage = []

    if data_for_storage is None:
        pass
    elif type(data_for_storage) == list:
        data_storage.extend(data_for_storage)
    else:
        data_storage.append(data_for_storage)

    # DON'T MODIFY THESE LINES.
    data_storage.append("data")
    return data_storage


def handle_exceptions(user_number):
    # Function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, returns `Yey! My number is higher!`,
    # returns `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    if type(user_number) == int and user_number > TEST_NUMBER:
        return 'Yey! My number is higher!'
    return 'Wow! My number is lower.'
