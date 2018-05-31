"""
This module describes an advanced example of basic metaclass analogues in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


Foo = type(
    "Foo",
    (),
    {
        "attr": 100,
        "attr_val": lambda x: x.attr
    }
)

x = Foo()
print(x.attr)
print(x.attr_val())


# This is the same as:
class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)
print(x.attr_val())

