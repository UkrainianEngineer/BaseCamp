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
    Implement this function!
    This function should convert decimal(integer) into binary.

    Args:
        n (int) - integer number to convert.

    Returns:
        int - integer number of binary representation for enterd n.
    """
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    else:
        return decimal_to_binary(n//2) + str(n%2)


def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    return int(str(n),2)


def storage(data_storage=[]):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.

    # DON'T MODIFY THESE LINES.
    data_storage.append("data")
    return data_storage


def handle_exceptions(user_number):
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.
    try:
        if user_number >  TEST_NUMBER:
            return 'Yey! My number is higher!'
        else:
            return 'Wow! My number is lower.'
    except TypeError:
        print('Enter correct number')
