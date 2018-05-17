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
    bin_n = 0
    i = 0
    while n > 0:
        bin_n += (n % 2) * pow(10, i)
        n = n/2
        i += 1
    return bin_n



def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    int_n = 0
    i = 0
    while n > 0:
        int_n += (n % 10) * pow(2, i)
        n = n / 10
        i += 1
    return int_n




def storage(data_storage = []):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.

    # DON'T MODIFY THESE LINES.
    # data_storage.append("data")
    # return data_storage
    data_storage.append('data')

    return data_storage


def handle_exceptions():
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    # ADD YOUR CODE HERE.
    while True:
        try:
            user_number = int(input("Please enter your nubmer: "))
            if user_number > TEST_NUMBER:
                print 'Yey! My number is higher!'
            elif user_number < TEST_NUMBER:
                print 'Wow! My number is lower!'
            break
        except ValueError:
            print "You didn't entered the number"







