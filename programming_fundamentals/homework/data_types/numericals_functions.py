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
        int - integer number of binary representation for entered n.
    """

    d2b = ''
    while n > 0:
        d2b += str(n & 1)
        n = n >> 1
    return int(d2b[::-1])


def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    b2d = 0
    for digit in str(n):
        b2d = b2d * 2 + int(digit)
    return b2d


def storage(data_storage=[]):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]
    # DON'T MODIFY THESE LINES.
    if 'data' not in data_storage:
        data_storage.append("data")
    return data_storage


def handle_exceptions(user_number):
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    # ADD YOUR CODE HERE.
    try:
        if int(user_number) > TEST_NUMBER:
            return "Yey! My number is higher!"
        else:
            return "Wow! My number is lower."
    except (TypeError, ValueError):
        return "Handled exception"
