"""
This module describes a basic example of Python's class instance.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Dog:
    """
    This is a basic class with list of class' attributes.
    """
    # Class attribute.
    is_alive = True

    def __init__(self, name, age):
        """
        Instance's attributes initialization goes here.
        """
        self.name = name
        self.age = age

if __name__ == '__main__':
    name = "Jackie"
    age = 2
    first_dog = Dog(name, age)
    second_dog = Dog(name, age)
    print(first_dog == second_dog)
