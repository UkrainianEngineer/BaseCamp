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

USER_INFO1 = {
    "name": "Pavlo",
    "surname": "Ivanchyshyn",
    "age": 28,
    "city": "Lviv"
}

def find_sum(something_should_be_there):
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
    pass
# ADD YOUR CODE HERE.
def suma (a, b, *ad) :
    h = a + b
    for i in ad :
        h +=i
    return h
print ('Функція сумми перемінної кількості аргументів: ' + str(suma(1, 2, 5, 6, 7)))


dic = {'num1' : 1, 'num2' : 2}

def suma2 (a, b, **ad) :
    h = a + b
    return h, dic
print ('Функція сумми перемінної кількості аргументів: ' + str(suma2(1, 2, **dic)))


def write_to_file():
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    ofile = open(input('Enter adress to file. If file doesent exist, it will be create, if file exist, it will be rewrite!: '), 'w')
    ofile.write(input('Enter text for write in this file: ') + '\n')
    print('Success!')
    ofile.close

#write_to_file()

def read_file():
    """
    Implement this function!
    This function should read all the lines from the file with `filename`.

    Args:
        filename (str) - name of file for writing.

    Returns:
        list - list of lines from the file.
    """
    # ADD YOUR CODE HERE.
    ofile = open(input('Enter adress to file for open: '), 'r')
    print('Info about file: ' + str(ofile))
    print(ofile.read())
    ofile.close

#read_file()

def append_to_file():
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    adr = input('Enter adress to file for append: ')
    ofile = open(adr, 'r')
    print(ofile.read())
    ofile.close
    ofile = open(adr,'a')
    ofile.write(str(input('What would you like to append to this file? ')))
    ofile.close
    ofile = open(adr, 'r')
    print('New file: ' + ofile.read())
    ofile.close

#append_to_file()

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
    with open (filename, 'w') as fn :
        fn.write('Hi there! \nMy name is {} {}. \nI am {} years old. I live in {}.'.format(USER_INFO['name'], USER_INFO['surname'], USER_INFO['age'], USER_INFO['city']))
        print('File red')

USER_INFO = {
    "name": "Vitalik",
    "surname": "Kosiak",
    "age": 23,
    "city": "Lviv"
}
filename = '2.txt'        
#write_user_info(filename, USER_INFO)    

def get_user_info():
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
    filename = input('Enter adress to file for get user info: ')
    with open (filename, 'r') as fn :
        tstr = fn.read().lower()
        tstr = tstr.split()
        print(tstr)
        
    info = {'name' : '','surname': '','age': '','city': ''}
    info['name'] = (tstr[tstr.index('is') + 1]).title()
    info['surname'] = (tstr[tstr.index('is') + 2]).title()
    info['age'] = (tstr[tstr.index('am') + 1]).title()
    info['city'] = (tstr[tstr.index('in') + 1]).title()

    print(info)
       
    #fn = open(filename)
    #for line in fn:
        #print(line)
     
get_user_info() 
