"""
This module describes good example of using complicated logic with documentation.
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
    """
    Writes code following these steps:
    1. Create a space for coding.
    2. Get some inspiration.
    3. Loop through some hours of effort.
    4. Write some code.
    5. Pull out hair cause of bugs.
    """
    code = Code()
    inspiration = Inspiration()
    for hour in Effort():
        try:
            code += hour + inspiration
        except CurseWorthyBug:
            # Something is handling here is some way.
            pass
