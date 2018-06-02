"""
This module describes a homework related to User's permissions verification.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

import time

# This is a task for creating a proper program design to resolve the task.
# The final solution should be implemented according to all code styles, etc.
# and all provided requirements.

# You should create a classes, functions, etc. by yourself.

# As a result we should have an activity log with all the information.
# Activity log - text file.
LOG_FILE = 'log.txt'


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.page = None

    def set_group(self, new_role):
        """
        Function sets new role for user.
        """
        self.role = new_role

    def check_permissions(self, page):
        """
        Function checks the user's permissions on the page.
        :param page: page instance
        :return: (bool)
        """
        self.page = page.page_name
        if self.role in page.permissions:
            return True
        else:
            return False

    def login(self):
        """
        Function writes a success message into activity log.
        """
        message = "[{}] User '{}' has been successfully logged in '{}' page."
        return Logger.write_log(self.name, self.page, message)

    def logout(self):
        """
        Function writes an error message into activity log.
        """
        message = "[{}] User '{}' has not enough permissions for '{}' page."
        return Logger.write_log(self.name, self.page, message)


class Page:
    def __init__(self, page_name):
        self.page_name = page_name
        self.permissions = []

    def allow_for(self, user_groups=None):
        """
        Function sets what user groups can have access to a page
        :param user_groups: (list) list with user groups
        """
        if user_groups is None:
            self.permissions = []
        else:
            self.permissions = user_groups.copy()


class Logger:
    @staticmethod
    def write_log(username, page, message):
        """
        Function writes a message to LOGFILE.
        :param username: (str)
        :param page: (str) сurrent page name
        :param message: (str) message template
        """
        try:
            with open(LOG_FILE, 'a') as log:
                current_time = time.strftime("%d %b %Y %H:%M:%S", time.gmtime())
                entry = message.format(current_time, username, page)
                log.write(entry + '\n')
        except (IOError, OSError) as exp:
            print(exp)


admin_user = User("Pavlo", "admin")
moderation_user = User("Yura", "moderator")
regular_user = User("Max", "regular")
regular_user.set_group("moderator")

page = Page("Settings")
page.allow_for(['admin', 'moderator'])

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
