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
    a = []
    k = n
    while k > 0:
        if (k % 2) == 1:
            a.append(1)
            k = k // 2
        else:
            a.append(0)
            k = k/2
    a.reverse()
    a = int("".join(str(x) for x in a))
    print(str(n)+" in binary representation is "+str(a))

decimal_to_binary(TEST_NUMBER)


def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    D = 0
    k = str(n)
    for index, x in enumerate(k):
        D = D + int(x)* 2**(len(k)- index - 1)
    print(str(n) + " in decimal is equal to " + str(D))
     
binary_to_decimal(101010)


def storage(something_should_be_here):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.
    data_storage = something_should_be_here

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
    else:
        if number > TEST_NUMBER:
            return 'Yey! My number is higher!'
        elif number < TEST_NUMBER:
            return 'Wow! My number is lower.'
        else:
            return 'It is a correct answer. '

m = handle_exceptions(42)
print(m)
