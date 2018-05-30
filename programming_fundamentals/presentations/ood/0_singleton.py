"""
This module describes a basic example of singleton in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Singleton it's a class, only one instance of which should be created.
# There is no possibility to create two or more different instances.
# Singleton is often used for database connections, etc.


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls)
        return cls.instance

# This is a simple usage of our singleton.
singleton = Singleton()
print(id(singleton))
# It returns the same object.
new_singleton = Singleton()
print(id(new_singleton))
