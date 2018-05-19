"""
This module describes basic example with appending to the text file.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

print("File content before appending: ")
data = open('testfile.txt', 'r')
print(data.read())
data.close()

f = open('testfile.txt', 'a')
print("Appending to the file...")
f.write("One more thing.")
f.close()

print("File content after appending: ")
data = open('testfile.txt', 'r')
print(data.read())
data.close()
