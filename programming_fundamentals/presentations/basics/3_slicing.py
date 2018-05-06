"""
This module describes basic examples of slicing in Python.
"""
from utils import prepare_output

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


example_list = ['one', 1, 2.0, True, [0.1, 0.2, 0.3]]
example_list[0] == 'one'
example_list[1] == 1
example_list[4][1] == 0.2

print("Original list: {}".format(example_list))

print(prepare_output("example_list[2:4]", example_list[2:4]))  # [2.0, True]
print(prepare_output("example_list[3:]", example_list[3:]))  # [True, [0.1, 0.2, 0.3]]
print(prepare_output("example_list[:5]", example_list[:5]))  # ['one', 1, 2.0, True, [0.1, 0.2, 0.3]
print(prepare_output("example_list[1:5:2]", example_list[1:5:2]))  # [1, True]
