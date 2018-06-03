"""
This module describes a very basic example of basic metaclass analogues in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


Foo = type("Foo", (), {})
x = Foo()

Bar = type("Bar", (Foo,), dict(attr=100))

x = Bar()
print(x.attr)


# This is the same as:
class Foo:
    pass


class Bar(Foo):
    attr = 100

x = Bar()
print(x.attr)

