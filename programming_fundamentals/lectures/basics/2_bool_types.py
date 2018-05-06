"""
This module describes basic boolean type conversions in Python.
"""
from utils import prepare_output

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# This block describes False values in Python.
print("=" * 60)
print("This block describes `False` expressions.")
print("=" * 60)
print(prepare_output("bool(None)", bool(None)))
print(prepare_output("bool(0)", bool(0)))
print(prepare_output("bool(0.0)", bool(0.0)))
print(prepare_output("bool('')", bool('')))
print(prepare_output("bool(False)", bool(False)))

print("=" * 60)
print("This block describes `True` expressions.")
print("=" * 60)
print(prepare_output("bool(1)", bool(1)))
print(prepare_output("bool(10)", bool(10)))
print(prepare_output("bool(-1.1)", bool(-1.1)))
print(prepare_output("bool('False')", bool('False')))
print(prepare_output("bool(-100500)", bool(-100500)))

