"""
This module describes a basic example of context manager in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Context manager describes some activities which might be done
# before and after code execution.
# It is very useful for cases when all objects of class should
# prepare some data or close/remove something.


class CustomContext:
    def __enter__(self):
        # This is done before your code in `with` block.
        print("Entered...")

    def __exit__(self, exception_type, exception_value, traceback):
        # This is done after your code in `with` block.
        print("Exited...")

# This is a simple usage of our context manager.
with CustomContext():
    print("Custom message goes here.")
