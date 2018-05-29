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


#def decimal_to_binary(n):
"""
Implement this function!
This function should convert decimal(integer) into binary.
Args:
n (int) - integer number to convert.
Returns:
int - integer number of binary representation for enterd n.

"""
#pass
    
#######################################################    
#inp_num = input("Please enter dec numb_ ")

def decimal_to_binary (dec_num) :
    try:
        dec_num = int(dec_num)
    except (ValueError) :
        print("Only dec numb!!!")
    res = ""
    while dec_num > 0 :
        temp = str(dec_num % 2)
        res = temp + res
        dec_num = int(dec_num / 2)
    return res

#print (dec_to_bin(inp_num))
####################################################### 

#def binary_to_decimal(n):
    """
    Implement this function!
    This function should convert binary into integer(decimal).

    Args:
        n (int) - binary representation of a number.

    Returns:
        int - decimal representation of a proper number.
    """
    #pass
####################################################### 
def binary_to_decimal (num) :
    try:
        num = int(num)
    except (ValueError):
        print("Wrong number!")

    st = str(num) #input number
    le = len(st) #lenght of input number it need for culc.

    i = 0 #count var whole num
    res = 0 #var of result

    while i <((len(st))) : #expression
        k = 0 #count var diff num
        temp = (int(st[i])) #take num
        if temp == 0 or temp == 1 : #check num for bin
            while k < ((len(st)) - i - 1) : #expression
                temp = temp* 2 #mull
                k = k+1 #count iter
                #print(temp)
        
            res = res + temp #calc result
            i = i + 1
        else:
            print("Only '1' and '0' num!!!")
            res = 0
            break
    return(res)

#print(bin_to_hex(input('Enter bin num_ '))) 
#######################################################

data_storage = []

def storage(*inp_data):
    # Your function should return list with added `data` value
    # into passed list into function or just `data` value in empty list.
    # Example:
    # storage([]) -> ["data"]
    # storage() -> ["data"]
    # storage(["test"]) -> ["test", "data"]

    # Change parameters in function for needed.
    # Also you is able to add some additional code here if needed.
    if len(inp_data) > 0:
        data_storage.append(inp_data)
    # DON'T MODIFY THESE LINES.
    data_storage.append('data')
    return data_storage


def handle_exceptions(user_number):
    # Write a function which uses `user_number` as a value entered by user.
    # If their number is higher than `TEST_NUMBER`, return `Yey! My number is higher!`,
    # return `Wow! My number is lower.` otherwise.
    # Handle possible exceptions.

    # ADD YOUR CODE HERE.
    try :
        if user_number > TEST_NUMBER :
            return 'Yey! My number is higher!'
        else :
            return 'Wow! My number is lower'
    except TypeError :
        return 'Use only integer number!!!'
    except SyntaxError :
        return 'Dont use special symbols!! Only number!!'
    except NameError :
        return 'Only number!! As 1 or 4 or 51!'
    except :
        return 'Unknown error!'
    
