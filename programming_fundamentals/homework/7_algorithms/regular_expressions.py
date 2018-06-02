"""
This module describes a homework related to URL validation via regular expressions.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

import re

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

def is_valid_url(url):
    regex = re.compile("http([s]?)://facebook.com/[a-z_.]+/[a-z]+$")
    return bool(re.match(regex, url))

# Example of usage:
#
# is_valid_url("https://facebook.com/pivanchy/allactivity")  # Returns `True`.
# is_valid_url("https://facebook.com/pivanchy")  # Return `False`.
# is_valid_url("https://facebook.com/pivanchy/allactivity/info")  # Returns `False`.
# is_valid_url("https://facebook.com/allactivity")  # Returns `False`.'
#
# 2. Second task.
# Using a URLs from the first task, create another regular expression,
# which helps to SEARCH User's ID from provided URL.
# This task should be wrapper into `get_user_id` function.
#

def get_user_id(url):
    regex = re.compile("//facebook.com/([a-z_.]+)/")
    user_id = re.search(regex, url)
    return (user_id.groups()[0])

# Example of usage:
#
# get_user_id("http://facebook.com/pivanchy/allactivity")  # Expected output is `pivanchy`.
# get_user_id("https://facebook.com/pivanchy/allactivity")  # Expected output: `pivanchy`.
