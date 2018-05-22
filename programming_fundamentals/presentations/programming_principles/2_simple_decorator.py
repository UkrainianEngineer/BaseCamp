"""
This module describes a very basic example of decorator in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def decorator_func(some_func):
    # Define another wrapper function which modifies some_func.
    def wrapper_func():
        print("Wrapper function started")
        some_func()
        print("Wrapper function ended")

    return wrapper_func


def say_hello():
    print("Hello")


say_hello = decorator_func(say_hello)
say_hello()



