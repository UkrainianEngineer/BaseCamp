#!/usr/bin/env python
"""
This module contains tasks related to arguments & parameters, files in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
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
    "name": "Pavlo",
    "surname": "Ivanchyshyn",
    "age": 28,
    "city": "Lviv"
}


def find_sum(*args):
    """
    This function sums of numbers for different amount of parameters.
    It is similar to built-in `sum` function.
    DON'T use `sum` function here.

    Returns: int - sum of numbers.
    Examples:
        find_sum(1, 2, 3)  # Returns 6.
        find_sum(1)  # Returns 1.
        find_sum([1, 3])  # Returns 4.
        find_sum(1, 2, 3, 4, 5, 6)  # Returns 21.
        etc.
    """
    summ = 0

    for arg in args:
        if isinstance(arg, list):
            for i in arg:
                summ += i
        else:
            summ += arg

    return summ


def write_to_file(filename, data):
    """
    This function writes all the lines from `data` into file with `filename`.
    Args: filename (str) - name of file for writing.
          data (list, tuple) - lines of text which should be added into file.
    """

    with open(filename, 'w') as new_file:
        for line in data:
            new_file.write(line + '\n')


def read_file(filename):
    """
    This function reads all the lines from the file with `filename`.
    Args: filename (str) - name of file for writing.
    Returns: list - list of lines from the file.
    """

    with open(filename, 'r') as file_to_read:
        file_content = file_to_read.readlines()

    return file_content


add_data = ('some additional info', 'for this file')


def append_to_file(filename, data):
    """
    This function appends lines from `data` into the file with `filename`.
    Args: filename (str) - name of file for writing.
          data (list, tuple) - lines of text which should be added into file.
    """

    with open(filename, 'a') as file_to_change:
        for line in data:
            file_to_change.write(line + '\n')


def write_user_info(filename, data):
    """
    Using function `write_to_file` do the following:
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

    greeting = 'Hi there!'
    name = 'My name is {} {}.'.format(data['name'], data['surname'])
    age = 'I am {} years old.'.format(data['age'])
    city = 'I live in {}.'.format(data['city'])

    info_for_file = [greeting, name, age, city]

    write_to_file(filename, info_for_file)


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

    all_words = []

    with open(filename, 'r') as file_to_read:
        file_content = file_to_read.readlines()

    for i in file_content:
        for t in i.split():
            all_words.append(t)

    user_info = {
        "name": all_words[5],
        "surname": all_words[6][:-1],
        "age": all_words[9],
        "city": all_words[15][:-1]
    }

    return user_info


