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
    jackie = Dog("Jackie", 2)
    funky = Dog("Funky", 8)
    print("{} is {} years old and {} is {} years old.".format(
        jackie.name,
        jackie.age,
        funky.name,
        funky.age
    ))

    # Check if Jackie is alive.
    if jackie.is_alive:
        print("{} is alive!".format(jackie.name))
    else:
        print("{} is not alive. ;(".format(jackie.name))
