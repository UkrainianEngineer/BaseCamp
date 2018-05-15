"""
This module describes basic examples with parameters and arguments in Python.
Also it demonstrates a very simple cases with *args and **kwargs.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


def read_file(filename, mode='w', *args, **kwargs):
    """
    This function contains:
        - one required parameter called `filename`,
        - one optional parameter called `mode` with a default value,
        - var-positional parameters called *args,
        - var-keyword parameters called **kwargs.
    """
    print("Filename is: {}".format(filename))
    print("Mode is: {}".format(mode))
    print("Args: {}".format(args))
    print("Kwargs: {}".format(kwargs))


print("Function declaration: `def read_file(filename, mode='w', *args, **kwargs):`")
print("Function call looksl like: `read_file('test.log', 'r', (100, 20000), use_buffer=True)`")
file_data = read_file('test.log', 'r', (100, 20000), use_buffer=True)


