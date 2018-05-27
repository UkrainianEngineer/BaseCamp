"""
This module describes a basic example of Python's class with attributes.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Dog:
    """
    This is a basic class with list of attributes.
    ALl these attributes would be assigned into Dog's instances.
    """
    def __init__(self, name, age):
        """
        Instance's attributes initialization goes here.
        """
        self.name = name
        self.age = age
