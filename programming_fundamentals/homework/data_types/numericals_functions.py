#!/usr/bin/env python
"""
This module contains tasks related to data types in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

import copy
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
    return int("{0:b}".format(int(n)))



def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    return int(str(n), 2)


def storage(arg=None):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.

    # DON'T MODIFY THESE LINES.

    data_storage = []
    if type(arg) is list:
        arg.append("data")
        data_storage = copy.copy(arg)
    elif arg is None:
        data_storage.append("data")
    else:
        data_storage.append(arg)
        data_storage.append("data")
    return data_storage


def handle_exceptions(user_number):
    try:
        if int(user_number) > TEST_NUMBER:
            return "Yey! My number is higher!"
        else:
            return "Wow! My number is lower."
    except (TypeError, ValueError):
        return "Wow! My number is lower."

