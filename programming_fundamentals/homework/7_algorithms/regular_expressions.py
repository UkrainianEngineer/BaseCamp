import re


def is_valid_url(url):
    pattern = "https?://facebook.com/([^/]*)/([^/]*)$"
    m = re.search(pattern, url)

    if m is None:
        return "False"
    else:
        return "True"


def get_user_id(url):
    pattern = "https?://facebook.com/([^/]*)/([^/]*)$"
    m = re.search(pattern, url)

    if m is None:
        return ""
    else:
        return m.group(1)


print (is_valid_url("https://facebook.com/pivanchy/allactivity"))
print(is_valid_url("https://facebook.com/pivanchy"))
print(is_valid_url("https://facebook.com/pivancy/allactivity/info"))
print(is_valid_url("https://facebook.com/allactivity"))
print(get_user_id("https://facebook.com/pivancy/allactivity"))
print(get_user_id("https://facebook.com/pivancy/allactivity"))
