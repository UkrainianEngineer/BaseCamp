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
        self.page_name = None

    def write_to_log(self, text):
        with open("log.txt", 'a') as fp:
            fp.write(text)

    def set_group(self, new_group_name):
        self.group = new_group_name

    def check_permissions(self, page_obj):
        self.page_name = page_obj.page_name
        if self.group in page_obj.allowed_group:
            return True
        else:
            return False

    def login(self):
        User.write_to_log(self, "User {} has been successfully logged in {} page.".format(self.name, self.page_name) + "\n")

    def logout(self):
        User.write_to_log(self, "User {} has not enough permissions for {} page.".format(self.name, self.page_name) + "\n")


class Page:
    def __init__(self, page_group):
        self.allowed_group = self.page_name = page_group

    def allow_for(self, group_list):
        self.allowed_group = group_list.copy()


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
    admin_user.login()
else:
    # Logout should write an error message into activity log.
    # It might be something similar to:
    # User `Pavlo` has not enough permissions for `Settings` page.
    admin_user.logout()
