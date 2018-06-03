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
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def set_group(self,group):
        self.group = group
    def check_permissions(self, selected_page):
        """
        This method verifies if role of the passed
        object is enumerated in the passed page list
        of allowed users.
        """
        if self.role in selected_page.allowed_users:
            return True
        else: return False
    def login(self, page):
        """
        This method creates and writes to a file
        a messagge on successful logging in.
        """
        filename = "activity_log_{}.txt".format(self.name)
        message = "User {} has been successfully logged into {} page."
        with open(filename, "w") as log:
            log.write(message.format(self.name, page.title))
    def logout(self, page):
        """
        This method creates and writes to a file
        a messagge on unsuccessful logging in due to
        lack of permissions.
        """
        filename = "activity_log_{}.txt".format(self.name)
        message = "User {} has not enough permissions for {} page."
        with open(filename, "w") as log:
            log.write(message.format(self.name, page.title))


class Page:
    def __init__(self, title):
        self.title = title
    def allow_for(self, users_list):
        """
        This method creates an instance attribute
        of allowed users and passes a list to it.
        """
        self.allowed_users = users_list


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
