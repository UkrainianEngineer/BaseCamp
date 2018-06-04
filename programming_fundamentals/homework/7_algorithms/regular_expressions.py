"""
This module describes a homework related to URL validation via regular expressions.
"""

import re

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# 1. First task.
# Create a regular expression which MATCHES the following URL:
# https://facebook.com/<username>/allactivity
#
# Where <username> - your facebook ID (or something like `zuck`).
#
# Your expression should work also for other User's pages, like:
# https://facebook.com/<username>/friends
# and so on.
#
# Also your expression should work without changes for:
# http://facebook.com/<username>/allactivity
# This task should be wrapped into `is_valid_url` function.
#
# 2. Second task.o
# Using a URLs from the first task, create another regular expression,
# which helps to SEARCH User's ID from provided URL.
# This task should be wrapper into `get_user_id` function.
# Example of usage:
regex = re.compile(r"(?<=\.com/)([a-z]+\.?[a-z]+)(?=\/{1}[a-z]+$)")


def is_valid_url(string, regex):
    url = re.search(regex, string)
    if url:
        return True
    else:
        return False


def get_user_id(string, regex):
    user_id = re.findall(regex, string)
    return user_id[0]


print(is_valid_url("https://facebook.com/yura.kekc/allactivity", regex))  # Returns `True`.
print(is_valid_url("https://facebook.com/yura.kekc", regex))  # Return `False`.
print(is_valid_url("https://facebook.com/yura.kekc/allactivity/info", regex))  # Returns `False`.
print(is_valid_url("https://facebook.com/allactivity", regex))  # Returns `False`.'
print(get_user_id("http://facebook.com/yura.kekc/allactivity", regex))  # Expected output is `yura.kekc`.
print(get_user_id("https://facebook.com/yura.kekc/allactivity", regex))  # Expected output: `yura.kekc`.
