"""
This module describes how `tuple` type behaves in Python.
It is important to understand how to work with mutable and immutable types.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

pack = ("Hello", "world")
print("Original value => {}".format(pack))
starting_id = id(pack)
pack = pack + ("!", "Have", "fun")
ending_id = id(pack)
print("ID of an original object => {}".format(starting_id))
print("Changed value => {}".format(pack))
print("ID of a changed object => {}".format(ending_id))
object_updated = starting_id == ending_id
print("Same object ID? {}".format(object_updated))
if object_updated:
    print("Current object has been updated!")
else:
    print("New object has been created!")
