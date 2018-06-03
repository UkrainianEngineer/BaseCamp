"""
This module describes a homework related to User's permissions verification.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"

import copy
import datetime

FILENAME = "user_activity.txt"
now = datetime.datetime.now()
time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
cache = []

# This is a task for creating a proper program design to resolve the task.
# The final solution should be implemented according to all code styles, etc.
# and all provided requirements.

# You should create a classes, functions, etc. by yourself.

# As a result we should have an activity log with all the information.
# Activity log - text file.


class User:

    userNumber = 0

    def __init__(self, name, group, page=None):
        self.name = name
        self.group = group
        self.page = page
        User.userNumber += 1

    def set_group(self, group):
        """
        This function set a new value for self.group variable
        """
        self.group = group

    def allow_for(allowed_groups):
        """
        This function as a decorator function checks
        if user has permission to open a page

        Args:
            function(func) - function to wrap
            allowed_groups(list) - additional parameter to decorator function
            page(obj) - instance of Page class

        Returs:
            function(func) - wrapped function
        """
        def decorator(function):
            def wrapper(self, *args, **kwargs):
                self.page = args[0].title
                if self.group in allowed_groups:
                    return function(self, *args, **kwargs)
            return wrapper
        return decorator

    @allow_for(cache)
    def check_permissions(self, page):
        """
        This function wrapped by *@allow_for* decorator function
        checks if user has permission to open page

        Args:
            page(obj) - instance of Page class
        """
        print("User {} has permission to  {} page.".format(self.name, self.page))
        return True

    def login(self):
        """
        This function return information about successful login of user.

        :param filename(str) - name of file for logs
        :param data(str) - message about successful login of user
        :param time(datetime) - time of user activity

        Returns:
            call of write_log() function
        """

        data = ("{} User {} has been successfully logged in {} page."
                .format(time, self.name, self.page))
        return User.write_log(self, data)

    def logout(self):
        """
        This function return information about failure login of user.

        :param filename(str) - name of file for logs
        :param data(str) - message about successful login of user
        :param time(datetime) - time of user activity

        Returns:
            call of write_log() function
        """
        data = ("{} User {} has not enough permissions for {} page."
                .format(time, self.name, self.page))
        return User.write_log(self, data)

    def write_log(self, data, filename=FILENAME):
        """ This function writes all information about user
            activity into `filename`.

        Args:
            filename (str) - name of file for writing.
            data (str) - text which should be added into file.
        """
        try:
            with open(filename, 'a') as file:
                file.write(data + '\n')
        except (OSError, IOError):
            raise Exception("An Error has occurred during handling the file!")

    def get_users_number(self):
        """
        This function return total number of user who signed into the site

        Returns:
            call 'write_log' function
        """
        data = "\n Number of users tried to sign into website is {}. \n".format(User.userNumber)
        return User.write_log(self, data)


class Page:

    def __init__(self, title, groups=None):
        self.title = title
        self.groups = groups

    def allow_for(self, groups=None):
        """
        This function set a new value for self.groups variable
        """
        self.groups = copy.copy(groups)
        global cache
        for el in self.groups:
            cache.append(el)


admin_user = User("Pavlo", "admin")
moderation_user = User("Yura", "moderator")
regular_user = User("Max", "regular")
regular_user.set_group("moderator")
new_regular_user = User("Oksana", "regular")

page = Page("Settings")
page.allow_for(["admin", "moderator"])


def check_user(user):
    is_allowed = user.check_permissions(page)
    if is_allowed:
        user.login()
    else:
        user.logout()


check_user(admin_user)
check_user(moderation_user)
check_user(regular_user)
check_user(new_regular_user)
# admin_user.get_users_number()
