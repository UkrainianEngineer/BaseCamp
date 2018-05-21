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
    summ = 0
    for element in args:
        summ = summ + element
    return summ

def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'w') as a_file:
        for item in data:
            a_file.write(item + '\n')

#write_to_file('FILENAME', lines)

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
    with open(filename, 'r') as a_file:
        output = []
        for lines in a_file:
            output.append(lines.rstrip())
        return output
#print(read_file('FILENAME'))

def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'a') as a_file:
        for item in data:
            a_file.write(item + '\n')
#append_to_file('FILENAME', lines)

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
    text = ['Hi there!',
    'My name is <name> <surname>.',
    'I am <age> years old.',
    'I live in <city>.']

    text[1] = text[1].replace('<name>', data['name'])
    text[1] = text[1].replace('<surname>', data['surname'])
    text[2] = text[2].replace('<age>', str(data['age']))
    text[3] = text[3].replace('<city>', data['city'])

    write_to_file(filename, text)

write_user_info('FILENAME', USER_INFO)

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
    with open(filename) as a_file:
        text = a_file.read().split('\n')
    
    #Function get_substring() finds string between two substrings
    def get_substring(whole, sub1, sub2):
        return whole[whole.index(sub1)+len(sub1)+1 : whole.index(sub2)]

    #Create empty dictionary named user_info
    user_info = {}

    #Add values to the dictionary for defined keys
    user_info['name'] = get_substring(text[1], 'is', '.').split(' ')[0]
    user_info['surname'] = get_substring(text[1], 'is', '.').split(' ')[1]
    user_info['age'] = get_substring(text[2], 'am', 'years')
    user_info['city'] = get_substring(text[3], 'in', '.')
    
    return user_info
   
#print(get_user_info('FILENAME'))
