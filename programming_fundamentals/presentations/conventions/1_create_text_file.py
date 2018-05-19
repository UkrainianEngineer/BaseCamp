"""
This module describes basic examples with creating a text file.
Also it demonstrates a very basic flow of work with files:open, write, close.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


f = open('testfile.txt', 'w')
print("Created a new file...")
f.write("Hello, world!")
f.write("How are you doing?")
f.write("It's an amazing file!")
f.close()
print("File descriptor has been closed.")


