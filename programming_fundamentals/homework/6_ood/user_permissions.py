"""
This module describes a homework related to User's permissions verification.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# This is a task for creating a proper program design to resolve the task.
# The final solution should be implemented according to all code styles, etc.
# and all provided requirements.

# You should create a classes, functions, etc. by yourself.

# As a result we should have an activity log with all the information.
# Activity log - text file.

class User:
    last_page = None

    def __init__(self, n, g):
        self.name = n
        self.group = g

    def set_group(self, g):
        self.group = g

    def check_permissions(self, p):
        allowed = 0
        for group_name_allowed in p.groups:
            if group_name_allowed == self.group:
                allowed = 1
        self.last_page = p
        return allowed

    def login(self):
        print ("User '{}' logged into page '{}'".format(self.name, self.last_page.name))

    def logout(self):
        print ("User '{}' did not have permissions to log into page '{}'".format(self.name, self.last_page.name))


class Page:
    groups = ["none"]
    name = ""

    def __init__(self, n):
        self.name = n

    def allow_for(self, group_array):
        self.groups = group_array


admin_user = User("Pavlo", "admin")
moderation_user = User("Yura", "moderator")
regular_user = User("Max", "regular")
# regular_user.set_group("moderator")

page = Page("Settings")
page.allow_for(["admin", "moderator"])

# is_allowed_admin = admin_user.check_permissions(page)
is_allowed_admin = regular_user.check_permissions(page)

if is_allowed_admin:
    # admin_user.login()
    regular_user.login()
else:
    # admin_user.logout()
    regular_user.logout()
