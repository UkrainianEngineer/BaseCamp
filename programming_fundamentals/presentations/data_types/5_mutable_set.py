"""
This module describes how `set` type behaves in Python.
It is important to understand how to work with mutable and immutable types.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

marks = {5.0, 4.9}
print("Original value => {}".format(marks))
starting_id = id(marks)
marks.add(3.9)
ending_id = id(marks)
print("ID of an original object => {}".format(starting_id))
print("Changed value => {}".format(marks))
print("ID of a changed object => {}".format(ending_id))
object_updated = starting_id == ending_id
print("Same object ID? {}".format(object_updated))
if object_updated:
    print("Current object has been updated!")
else:
    print("New object has been created!")
