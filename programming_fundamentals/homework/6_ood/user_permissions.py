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
        self.check_page = None

    def set_group(self, new_group):
        """
        This function set a new group into self.group variable

        Args:
            new_group (str): Write new group into group list.
        """
        self.group = new_group

    def check_permissions(self, check_page):
        """
        This function checks if user has permission to open this page

        Args:
            check_page(obj) - instance of class Page

        Returns:
            bool: - if we have permission or False if we haven't
        """
        self.check_page = check_page.page_title
        if self.group in check_page.allowed_groups:
            return True
        else:
            return False

    def login(self):
        """
        This function write information
        into file about successfully logging in.

        Returns:
            None
        """
        with open('activity_log.txt', 'a+') as f:
            f.write('User {} has not enough permissions for {} page.'
                    .format(self.name, self.check_page))

    def logout(self):
        """
        This function write information
        into file about unsuccessfully logging in.

        Returns:
            None
        """
        with open('activity_log.txt', 'a+') as f:
            f.write('User {} has not enough permissions for {} page.'
                    .format(self.name, self.check_page))


class Page:

    def __init__(self, page_title):
        self.page_title = page_title
        self.allowed_groups = []

    def allow_for(self, group_list):
        """
        Method gives permission for a page to particular user groups.

        Returns:
            None
        """
        for group in group_list:
            self.allowed_groups.append(group)


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
