"""
This module describes the home task related to numerical systems.
It might be useful for both students and mentors.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# This task is just for manual training.
# You should solve this task manually and verify the results using this script.
my_brth = '11111001001'
birthdate = int(input("Please enter a decimal year of your birth: "))
binary_date = input("Please enter your binary representation of decimal year of birth:")
assert "{0:b}".format(int(birthdate)) == str(binary_date), "Invalid answer. Please check your binary representation."
print("=" * 60)
print("Congratulations! You've done it!")
print("=" * 60)
