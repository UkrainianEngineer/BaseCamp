#!/usr/bin/env python
"""
This module contains tasks related to arguments & parameters, files in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
import re


__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

FILENAME = 'awesome_data.info'
lines = [
    "Two assure edward whence the was.",
    "Who worthy yet ten boy denote wonder.",
    "Weeks views her sight old tears sorry.",
    "Additions can suspected its concealed put furnished.",
    "Met the why particular devonshire decisively considered partiality.",
    "Certain it waiting no entered is.",
    "Passed her indeed uneasy shy polite appear denied.",
    "Oh less girl no walk.",
    "At he spot with five of view."
]

USER_INFO = {
    "name": "Yuriy",
    "surname": "Zhuk",
    "age": 25,
    "city": "Lviv"
}


def find_sum(*args):
    """
    Implement this function!
    This function should sum of numbers for different amount of parameters.

    It should be similar to built-in `sum` function.
    DON'T use `sum` function here.

    Returns:
        int - sum of numbers.

    Examples:
        find_sum(1, 2, 3)  # Returns 6.
        find_sum(1)  # Returns 1.
        find_sum([1, 3])  # Returns 4.
        find_sum(1, 2, 3, 4, 5, 6)  # Returns 21.
        etc.
    """
    # ADD YOUR CODE HERE.
    try:
        summ = 0
        for value in args:
            if isinstance(value, list):
                for val in value:
                    summ += int(val)
            else:
                summ += int(value)
        return summ
    except (TypeError, ValueError):
        return "Error, when the value is wrong"


def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'w') as file:
        for d in data:
            file.write(d + '\n')
    return


def read_file(filename):
    """
    Implement this function!
    This function should read all the lines from the file with `filename`.

    Args:
        filename (str) - name of file for writing.

    Returns:
        list - list of lines from the file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'r') as file:
        list_of_lines = file.readlines()
        return list_of_lines


def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'a') as file:
        for d in data:
            file.write(d + '\n')
    return


def write_user_info(filename, **kwargs):
    """
    Using functions: `write_to_file`, `read_file`, `append_to_file` do the following:
    - Create file with a `filename` name.
    - Write user's information from `data` into file with `filename` in the following format:

    Hi there!
    My name is <name> <surname>.
    I am <age> years old.
    I live in <city>.

    Where values in `<>` mean the keys from `data` object.

    Args:
        filename (str) - name of file for writing.
        data (dict) - personal user's information.
    """
    # ADD YOUR CODE HERE.
    # =====================================================
    # Example 1(this example doesn't work):
    # write_to_file(filename, text)
    # list_of_lines = read_file(filename)
    # for line in list_of_lines:
    #     if "{}" not in line:
    #         append_to_file(FILENAME, line)
    #         continue
    #     else:
    #         for key in kwargs:
    #             value = kwargs.get(key)
    #             line_with_value = line.format(value)
    #             append_to_file(FILENAME, line_with_value)
    # return

    # =======================================================
    # Example 2(work):
    kwargs = [
        "Hi there!",
        "My name is {} {}.".format(kwargs['name'], kwargs['surname']),
        "I am {} years old.".format(kwargs['age']),
        "I live in {}.".format(kwargs['city'])
    ]
    write_to_file(filename, kwargs)
    return


# write_user_info(FILENAME, **USER_INFO)


def get_user_info(filename):
    """
    Using file created by `write_user_info` create a reader. It should be able to read the following format:

    Hi there!
    My name is <name> <surname>.
    I am <age> years old.
    I live in <city>.

    Where values in `<>` mean the keys from `data` object.

    Args:
        filename (str) - name of file for writing.

    Returns
        dict - personal user's information.

    Example:
        get_user_info(FILENAME)  # Returns {"name": "Pavlo", "surname": "Ivanchyshyn", "age": 28, "city": "Lviv"}
    """
    # ADD YOUR CODE HERE.
    user_info = {
        "name": "",
        "surname": "",
        "age": "",
        "city": ""
    }
    pattern_one = r'\s(\w+\s\w+)\.'
    pattern_two = r'\d+'
    pattern_three = r'\s(\b\w+)\.'
    list_of_lines = read_file(filename)
    for index, line in enumerate(list_of_lines):
        if index == 0:
            continue
        elif index == 1:
            values = re.findall(pattern_one, line)
            fullname = values[0]
            fullname = fullname.split(' ')
            user_info['name'] = fullname[0]
            user_info['surname'] = fullname[1]
            continue
        elif index == 2:
            values = re.findall(pattern_two, line)
            age = values[0]
            user_info['age'] = int(age)
            continue
        else:
            values = re.findall(pattern_three, line)
            city = values[0]
            user_info['city'] = str(city)
            break

    return user_info


# get_user_info(FILENAME)
