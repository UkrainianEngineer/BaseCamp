import re

"""
This module describes a homework related to URL validation via regular expressions.
"""

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
#
# 2. Second task.
# Using a URLs from the first task, create another regular expression,
# which helps to SEARCH User's ID from provided URL.
# This task should be wrapper into `get_user_id` function.
#
# Example of usage:
#
# get_user_id("http://facebook.com/pivanchy/allactivity")  # Expected output is `pivanchy`.
# get_user_id("https://facebook.com/pivanchy/allactivity")  # Expected output: `pivanchy`.

def is_valid_url(string):
    pattern = re.compile(r"http(s)?://(www.)*facebook\.com/\w+(\.\w+(\.\d+)*)*\/\w+$")
    match = re.match(pattern, string)
    if match:
        print("True")
    else:
        print("False")


is_valid_url("https://facebook.com/pivanchy/allactivity")  # Returns `True`.
is_valid_url("https://facebook.com/pivanchy")  # Return `False`.
is_valid_url("https://facebook.com/pivanchy/allactivity/info")  # Returns `False`.
is_valid_url("https://facebook.com/allactivity")  # Returns `False`.'
is_valid_url("https://www.facebook.com/irina.pavlik.92/allactivity")  # Returns `True`.
is_valid_url("https://www.facebook.com/irina.pavlik.92")  # Return `False`.
is_valid_url("https://www.facebook.com/irina.pavlik.92/allactivity/info")  # Returns `False`.

# version 1


def get_user_id(string):
    start_id = re.compile(r"\.com/")
    end_id = re.compile(r"/\w+$")
    return string[(re.search(start_id, string)).end():(re.search(end_id, string)).start()]

# version 2


def get_user_id_second(string):
    pattern_user_id = re.compile(r"[^com\/]\w+[\.\w+\d+]*(?=/allactivity)")
    match = re.findall(pattern_user_id, string)
    if match:
        return match[0]


print(get_user_id("http://facebook.com/pivanchy/allactivity"))  # Expected output is `pivanchy`.
print(get_user_id("https://facebook.com/pivanchy/allactivity"))  # Expected output: `pivanchy`.
print(get_user_id("http://facebook.com/irina.pavlik.92/allactivity"))  # Expected output is `irina.pavlik.92`.
print(get_user_id("https://facebook.com/irina.pavlik.92/allactivity"))  # Expected output: `irina.pavlik.92`.
print(get_user_id_second("http://facebook.com/pivanchy/allactivity"))  # Expected output is `pivanchy`.
print(get_user_id_second("https://facebook.com/pivanchy/allactivity"))  # Expected output: `pivanchy`.
print(get_user_id_second("http://facebook.com/irina.pavlik.92/allactivity"))  # Expected output is `irina.pavlik.92`.
print(get_user_id_second("https://facebook.com/irina.pavlik.92/allactivity"))  # Expected output: `irina.pavlik.92`.
