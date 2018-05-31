"""
This module describes a very basic example of regexp usage in Python.
"""
import re
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


regex = re.compile(r'st', re.IGNORECASE)
print(regex.match("test"))  # None
print(regex.search("test"))  # # <_sre.SRE_Match object; span=(2, 4), match='st'>
