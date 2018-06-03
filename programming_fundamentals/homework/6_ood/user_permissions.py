"""
This module describes a homework related to User's permissions verification.
"""
LOG_FILE = "activities.log"

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# This is a task for creating a proper program design to resolve the task.
# The final solution should be implemented according to all code styles, etc.
# and all provided requirements.

# You should create a classes, functions, etc. by yourself.

# As a result we should have an activity log with all the information.
# Activity log - text file.
class Logger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        """
        Method writes a message into log file.

        Args:
            message (str): Message to write into log file.

        Returns:
            None
        """
        try:
            with open(self.file, "a") as file:
                file.write(message)
        except (OSError, IOError):
            print("Cannot write to {}".format(self.file))


class User:
    _logger = Logger(LOG_FILE)

    def __init__(self, name, group="regular"):
        self.name = name
        self._group = group

    def check_permissions(self, page):
        """
        Method checks if user has permissions for a specified page.

        Args:
            page (Page): Page for checking permissions.

        Returns:
            bool: True if you have permissions, False otherwise.
        """
        self._page = page
        if self._group in page.allowed_user_groups:
            return True
        else:
            return False

    def set_group(self, group):
        """
        Method sets user group.

        Args:
            group (str): Group to be set.

        Returns:
            None
        """
        self._group = group

    def login(self):
        """
        Method enters page for which permissions were checked.

        Args:
            None

        Returns:
            None
        """
        log_message = "{} has successfully logged in {}.\n".format(self, self._page)
        self._logger.log(log_message)

    def logout(self):
        """
        Method disallows login into page for which permissions were checked.

        Args:
            None

        Returns:
            None
        """
        log_message = "{} has not enough permissions for {}.\n".format(self, self._page)
        self._logger.log(log_message)

    def __str__(self):
        return "User '{}'".format(self.name)


class Page:
    def __init__(self, title):
        self.title = title
        self.allowed_user_groups = set()

    def allow_for(self, user_groups):
        """
        Method gives permission for a page to particular user groups.

        Args:
            user_groups (list): User groups to grant access.

        Returns:
            None
        """
        self.allowed_user_groups.update(user_groups)

    def __str__(self):
        return "'{}' page".format(self.title)


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
