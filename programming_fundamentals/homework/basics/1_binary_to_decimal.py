"""
This module describes the hometask related to numerical systems.
It might be useful for both students and mentors.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

# This task is just for manual training.
# You should solve this task manually and verify the results using this script.
test_year = 11100111101
decimal_year = input("Please enter a decimal representation for {}:".format(test_year))
assert int(str(test_year), 2) == decimal_year, "Invalid answer. Please check your decimal representation."
print("=" * 60)
print("Congratulations! You've done it!")
print("=" * 60)

"""
Result: 1853
"""
