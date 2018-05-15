"""
This module describes basic example with iteration through a text file.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


try:
    f = open('testfile.txt', 'r')
    print("Reading a file...")
except FileNotFoundError:
    # Handle an exception if file does not exist.
    print("File does not exist. Please run `create_text_file.py` script before.")
else:
    # Print a file content if everything is OK.
    print("File content is:")
    for data in f:
        print(data)
