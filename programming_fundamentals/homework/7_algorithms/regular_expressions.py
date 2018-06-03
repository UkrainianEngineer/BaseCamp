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
#
# is_valid_url("https://facebook.com/pivanchy/allactivity")  # Returns `True`.
# is_valid_url("https://facebook.com/pivanchy")  # Return `False`.
# is_valid_url("https://facebook.com/pivanchy/allactivity/info")  # Returns `False`.
# is_valid_url("https://facebook.com/allactivity")  # Returns `False`.'

search_user_template = 'com\/(.+?)\/'
search_exception_template = 'com\/(.+?)\/(.+?)\/'


def is_valid_url(url=""):
    if re.search(search_user_template, url).group(1) is not None:
        if re.search(search_exception_template, url) is not None:
            return False
        return True
    else:
        return False


# 2. Second task.
# Using a URLs from the first task, create another regular expression,
# which helps to SEARCH User's ID from provided URL.
# This task should be wrapper into `get_user_id` function.
#
# Example of usage:
#
# get_user_id("http://facebook.com/pivanchy/allactivity")  # Expected output is `pivanchy`.
# get_user_id("https://facebook.com/pivanchy/allactivity")  # Expected output: `pivanchy`.

def get_user_id(url=""):
    if is_valid_url(url):
        return re.search(search_user_template, url).group(1)
    else:
        return "No valid name found"
