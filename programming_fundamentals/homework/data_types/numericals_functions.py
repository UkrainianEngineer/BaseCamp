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
    binary_form = []
    while n > 0:
        if (n % 2) == 1:
            binary_form.append(1)
            n = n // 2
        else:
            binary_form.append(0)
            n = n/2
    binary_form.reverse()
    binary_form = int("".join(str(x) for x in binary_form))
    return binary_form

print(decimal_to_binary(TEST_NUMBER))


def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    decimal_number = 0
    binary_number = str(n)
    for index, x in enumerate(binary_number):
        decimal_number = decimal_number + int(x)* 2**(len(binary_number)- index - 1)
    return decimal_number
     
print(binary_to_decimal(101010))


def storage(data=None):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.
    data_storage = []
    if data:
        data_storage += data

    # DON'T MODIFY THESE LINES.
    data_storage.append("data")
    return data_storage

print(storage(['test']))


def handle_exceptions(user_number):
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    # ADD YOUR CODE HERE.
    try:
        number = int(user_number)
    except ValueError:
        return "Function argument should be a number!"
    if number > TEST_NUMBER:
        return 'Yey! My number is higher!'
    elif number < TEST_NUMBER:
        return 'Wow! My number is lower.'

print(handle_exceptions('gh'))
