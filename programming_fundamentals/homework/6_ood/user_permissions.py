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
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.logfile = "logfile.txt"

    def set_group(self, group):
        self.group = group

    def check_permissions(self, page):
        if self.group in page.allowed_for:
            return True
        else:
            return False

    def login(self, page):
        with open(self.logfile, 'a') as f:
            f.write("User {} has been successfully logged in {} page.\n".format(self.name, page.name))
        
    def logout(self, page):
        with open(self.logfile, 'a') as f:
            f.write("User {} has not enough permissions for {} page.\n".format(self.name, page.name))

class Page:
    def __init__(self, name):
        self.name = name
        self.allowed_for = []
        
    def allow_for(self, groups):
        if not isinstance(groups, list):
            return "allow_for function accepts only lists"
        for user in groups:
            self.allowed_for.append(user)

admin_user = User("Pavlo", "admin")
moderation_user = User("Yura", "moderator")
regular_user = User("Max", "regular")
regular_user.set_group("moderator")

page = Page("Settings")
page.allow_for(["admin", "moderator"])

is_allowed_admin = admin_user.check_permissions(page)

if is_allowed_admin:
    # Login should write a success message into activity log.
    # It might be something similar to:
    # User `Pavlo` has been successfully logged in `Settings` page.
    admin_user.login(page)
else:
    # Logout should write an error message into activity log.
    # It might be something similar to:
    # User `Pavlo` has not enough permissions for `Settings` page.
    admin_user.logout(page)
