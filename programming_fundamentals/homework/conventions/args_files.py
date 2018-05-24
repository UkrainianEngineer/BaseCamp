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
    args_sum = 0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            args_sum += find_sum(*arg)
        elif isinstance(arg, (int, float)):
            args_sum += arg
    return args_sum


def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    try:
        with open(filename, 'w') as file:
            for line in data:
                file.write(line + '\n')
    except (OSError, IOError):
        print('File "{}" cannot be opened.'.format(filename))


def read_file(filename):
    """
    Implement this function!
    This function should read all the lines from the file with `filename`.

    Args:
        filename (str) - name of file for writing.

    Returns:
        list - list of lines from the file.
    """
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.rstrip())
    except (OSError, IOError):
        print('File "{}" cannot be opened.'.format(filename))
    return lines


def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    try:
        with open(filename, 'a') as file:
            file.write('\n'.join(data))
    except (OSError, IOError):
        print('File "{}" cannot be opened.'.format(filename))


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
    # ADD YOUR CODE HERE.
    user_info = ('Hi there!',
                 'My name is {name} {surname}.'.format(name=data.get('name', '___'),
                                                       surname=data.get('surname', '___')),
                 'I am {age} years old.'.format(age=data.get('age', '___')),
                 'I live in {city}.'.format(city=data.get('city', '___')))
    write_to_file(filename, user_info)


def get_user_info(filename):
    """
    Using file created by `write_user_info` create a reader. It should be able to read the following format:

    Hi there!
    My name is <name> <surname>.
    I am <age> years old.
    I live in <city>.

    Where values in `<>` mean the keys from `data` object.

    Args:
        filename (str) - name of file for reading.

    Returns
        dict - personal user's information.

    Example:
        get_user_info(FILENAME)  # Returns {"name": "Pavlo", "surname": "Ivanchyshyn", "age": 28, "city": "Lviv"}
    """
    # ADD YOUR CODE HERE.
    file_content = read_file(filename)

    if not file_content:
        return {}

    name_position = 3
    surname_position = 4
    age_position = 2
    city_position = 3

    user_info = {}
    for line in file_content:
        line = line.replace('.', '')
        words = line.split() 
        if 'My name is' in line:
            user_info['name'] = words[name_position]
            user_info['surname'] = words[surname_position]
        elif ('I am' in line) and ('years old' in line):
            user_info['age'] = int(words[age_position])
        elif 'I live in' in line:
            user_info['city'] = words[city_position]

    return user_info
