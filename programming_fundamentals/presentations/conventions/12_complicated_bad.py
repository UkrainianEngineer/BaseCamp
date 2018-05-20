"""
This module describes bad example of using complicated logic without documentation.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class Code(): pass


class Inspiration(): pass


class CurseWorthyBug(Exception): pass


class Effort():
    def __iter__(self):
        return (x for x in range(10))


def code():
    """Write some code."""
    code, inspiration = Code(), Inspiration()
    for hour in Effort():
        try:
            code += hour + inspiration
        except CurseWorthyBug:
            # Something is handling here is some way.
            pass
