"""
This module describes basic example with using context manager with a text file.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


with open('testfile.txt', 'r') as f:
    print("File content is:")
    print(f.read())
