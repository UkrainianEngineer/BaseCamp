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
    # Initialize sum as 0
    sum = 0

    for arg in args:
        # If element is list, then iterate over it's elements. But this will not work if a list is an element of another list
        if (type(arg) == type([])):
            for element in arg:
               sum = sum + element
        else:
            sum = sum + arg
    return (sum)

def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    # Open filename and clean it
    with open(filename, 'w') as f:
        # Iterate over all elements in a list or tuple and write it to FILENAME with EOL symbol
        # If it is the last element then do not add EOL symbol
        count = 0
        for line in data:
            if count != len(data) - 1:
                f.write(line + "\n")
                count = count +1
            else:
                f.write(line)
write_to_file(FILENAME, lines)

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
    with open(filename, 'r') as f:
        list = []
        for data in f:
            list.append(data)
    return list

def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    # Open filename for append
    with open(filename, 'a') as f:
        # Iterate over all elements in a list or tuple and write it to FILENAME
        for line in data:
            f.write("\n" + line)
append_to_file(FILENAME, lines)

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
    with open(filename, 'w') as f:
        f.write("Hi there!\nMy name is {} {}.\nI am {} years old.\nI live in {}.".format(data['name'], data['surname'],
                                                                                  data['age'], data['city']))
write_user_info(FILENAME, USER_INFO)

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
    user_info = {}
    # ADD YOUR CODE HERE.
    with open(filename, 'r') as f:
        for line in f:
            # If line contains 'My name is ' text then we store name and surname
            splitted_line = line.split("My name is ")
            if len(splitted_line) > 1:
                name_surname = splitted_line[1].split(" ")
                user_info['name'] = name_surname[0]
                user_info['surname'] = name_surname[1].split(".\n")[0]

            # If line contains 'I am' text then we store age
            splitted_line = line.split("I am ")
            if len(splitted_line) > 1:
                user_info['age'] = splitted_line[1].split(" ")[0]

            # If line contains 'I live in ' text then we store city
            splitted_line = line.split("I live in ")
            if len(splitted_line) > 1:
                user_info['city'] = splitted_line[1].split(".")[0]

    return user_info
print (get_user_info(FILENAME))
