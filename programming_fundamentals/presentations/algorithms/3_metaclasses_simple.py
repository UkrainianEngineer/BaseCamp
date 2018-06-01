"""
This module describes a very basic example of metaclasses usage in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Foobar:
    pass


print(type(Foobar))

foo = Foobar()
print(type(foo))

print(isinstance(foo, Foobar))
print(isinstance(Foobar, type))