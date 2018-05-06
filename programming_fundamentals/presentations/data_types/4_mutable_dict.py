"""
This module describes how `dict` type behaves in Python.
It is important to understand how to work with mutable and immutable types.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

info = {"name": "Pavlo", "surname": "Ivanchyshyn"}
print("Original value => {}".format(info))
starting_id = id(info)
info["age"] = 28
ending_id = id(info)
print("ID of an original object => {}".format(starting_id))
print("Changed value => {}".format(info))
print("ID of a changed object => {}".format(ending_id))
object_updated = starting_id == ending_id
print("Same object ID? {}".format(object_updated))
if object_updated:
    print("Current object has been updated!")
else:
    print("New object has been created!")
