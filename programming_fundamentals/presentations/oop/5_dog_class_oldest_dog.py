"""
This module describes a basic example of Python's class instance.
"""

from operator import attrgetter

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def get_the_oldest_dog(*dogs, check_alive=False):
    if check_alive:
        dogs = (dog for dog in dogs if dog.is_alive)
    return max(dogs, key=attrgetter('age'))


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
    dead_dog = Dog("Dead Dog", 22)
    dead_dog.is_alive = False

    oldest_alive_dog = get_the_oldest_dog(jackie, funky, dead_dog, check_alive=True)
    print("The oldest alive dog is {} with age {}.".format(
        oldest_alive_dog.name,
        oldest_alive_dog.age
    ))

    oldest_dog = get_the_oldest_dog(jackie, funky, dead_dog)
    print("The oldest dog is {} with age {}.".format(
        oldest_dog.name,
        oldest_dog.age
    ))