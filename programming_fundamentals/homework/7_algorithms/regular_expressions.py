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
# Example of usage:

def is_valid_url(string):
    regex = re.compile(r"(?<=\.com/)([a-z]+\.?[a-z]+)(?=\/{1}[a-z]+$)")
    url = re.search(regex, string)
    if url:
        return True
    else:
        return False


print(is_valid_url("https://facebook.com/yura.kekc/allactivity"))  # Returns `True`.
print(is_valid_url("https://facebook.com/yura.kekc"))  # Return `False`.
print(is_valid_url("https://facebook.com/yura.kekc/allactivity/info"))  # Returns `False`.
print(is_valid_url("https://facebook.com/allactivity"))  # Returns `False`.'


# 2. Second task.o
# Using a URLs from the first task, create another regular expression,
# which helps to SEARCH User's ID from provided URL.
# This task should be wrapper into `get_user_id` function.
#
# Example of usage:

def get_user_id(string):
    regex = re.compile(r"(?<=\.com/)([a-z]+\.?[a-z]+)(?=\/{1}[a-z]+$)")
    url = re.findall(regex, string)
    user_id = url[0]
    return user_id


print(get_user_id("http://facebook.com/yura.kekc/allactivity"))  # Expected output is `pivanchy`.
print(get_user_id("https://facebook.com/yura.kekc/allactivity"))  # Expected output: `pivanchy`.
