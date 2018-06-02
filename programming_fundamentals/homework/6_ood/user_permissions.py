import copy
import datetime
FILENAME = "user_activity.txt"
count = 0

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

    numberUsers = 0

    def __init__(self, name, user_group):
        self.name = name
        self.user_group = user_group
        User.numberUsers += 1

    def set_group(self, group):
        """This function set a new value for self.user_group variable"""
        self.user_group = group

    def check_permissions(self, page):
        """"This function check if user has permission to current page
        Args: page(obj) - instance of Page class"""

        self.page = page.page_name
        if self.user_group in page.groups:
            return True
        else:
            return False

    def login(self, filename=FILENAME):
        """This function return information about login success of user.
        Args: filename (str) - name of file for writing.
        return: func - write data to log file
        """
        data = ("{} User {} has been successfully logged in {} page."
                .format(datetime.datetime.now(), self.name, self.page))
        return User.write_to_log(self, data, filename=FILENAME)

    def logout(self, filename=FILENAME):
        """ This function return information about login failure of user.
        Args: filename (str) - name of file for writing.
        return: func - write data to log file
        """
        data = ("{} User {} has not enough permissions for {} page."
                .format(datetime.datetime.now(), self.name, self.page))
        return User.write_to_log(self, data, filename)

    def write_to_log(self, data, filename):
        """ This function writes all information about user activity into `filename`.
        Args:
            filename (str) - name of file for writing.
            data (str) - lines of text which should be added into file.
        """
        try:
            with open(filename, 'a') as file:
                file.write(data + '\n')
        except (OSError, IOError):
            print("An Error has occurred!")

    def get_users_number(self):
        """This function return total number of user who signed into the site """
        data = "Number of users signed into website is {}. \n".format(User.numberUsers)
        return User.write_to_log(self, data, filename=FILENAME)


class Page:

    def __init__(self, page_name, groups=None):
        self.page_name = page_name
        self.groups = groups

    def allow_for(self, groups=None):
        """This function set a new value for self.groups variable"""
        self.groups = copy.copy(groups)


class Test:

    admin_user = User("Pavlo", "admin")
    moderation_user = User("Yura", "moderator")
    regular_user = User("Max", "regular")
    regular_user.set_group("moderator")

    page = Page("Settings")
    page.allow_for(["admin", "moderator"])

    # admin_user.get_users_number()

    is_allowed_admin = admin_user.check_permissions(page)
    if is_allowed_admin:
        admin_user.login()
    else:
        admin_user.logout()
