"""
This module describes how `list` type behaves in Python.
It is important to understand how to work with mutable and immutable types.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

animals = ["cat", "dog"]
print("Original value => {}".format(animals))
starting_id = id(animals)
animals.append("snake")
ending_id = id(animals)
print("ID of an original object => {}".format(starting_id))
print("Changed value => {}".format(animals))
print("ID of a changed object => {}".format(ending_id))
object_updated = starting_id == ending_id
print("Same object ID? {}".format(object_updated))
if object_updated:
    print("Current object has been updated!")
else:
    print("New object has been created!")
