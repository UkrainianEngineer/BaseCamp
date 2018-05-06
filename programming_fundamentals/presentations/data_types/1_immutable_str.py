"""
This module describes how `str` type behaves in Python.
It is important to understand how to work with mutable and immutable types.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

name = "Pavlo"
print("Original value => {}".format(name))
starting_id = id(name)
name = name + " Ivanchyshyn"
ending_id = id(name)
print("ID of an original object => {}".format(starting_id))
print("Changed value => {}".format(name))
print("ID of a changed object => {}".format(ending_id))
object_updated = starting_id == ending_id
print("Same object ID? {}".format(object_updated))
if object_updated:
    print("Current object has been updated!")
else:
    print("New object has been created!")
