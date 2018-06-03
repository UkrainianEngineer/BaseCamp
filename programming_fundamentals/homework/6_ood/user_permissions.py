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
    """A user of site with a checking group. Users have the
       following properties:

       Attributes:
           name: A string representing the user's name.
           group: A string tracking the current group of the user.
       """

    def __init__(self, name, group):
        """
        Return a User object whose name is *name* and starting group is *group*.
        """
        self.name = name
        self.group = group
        self.check_page = None

    def set_group(self, new_group):
        """
        Assign a new group to the user.
        """
        self.group = new_group

    def check_permissions(self, check_page):
        """
        Allows you to check the access settings for the current user group.
        """
        self.check_page = check_page.page_tittle
        if self.group in check_page.allowed_groups:
            return True
        else:
            return False

    def login(self):
        """Logging login to the log file."""
        with open('activity_log.txt', 'a+') as log_file:
            log_file.write('User {} has been successfully logged in to {} page.\n'.format(self.name, self.check_page))

    def logout(self):
        """Logging logout to the log file."""
        with open('activity_log.txt', 'a+') as log_file:
            log_file.write('User {} have no enough permissions to login {} page.\n'.format(self.name, self.check_page))


class Page:
    """" A page of site with a list group. Page have the
       following properties:

       Attributes:
           page_tittle: A string representing the page name.
           allowed_groups: A string tracking the users groups that allowed to visit the page.
    """
    def __init__(self, page_tittle):
        """"
        Create a Page object whose name is *page_tittle* and starting group is *allowed_groups*.
        """
        self.page_tittle = page_tittle
        self.allowed_groups = []

    def allow_for(self, group_list):
        """
        Adding groups of users who are allowed to visit the page.
        """
        for i in group_list:
            self.allowed_groups.append(i)


admin_user = User("Pavlo", "admin")
moderator_user = User("Yura", "moderator")
regular_user = User("Max", "regular")

page = Page("Settings")
page.allow_for(["admin", "moderator"])


def is_allowed_user(user):
    """
    Main function to operate and login/logout users
    """
    check = user.check_permissions(page)
    if check:
        user.login()
    else:
        user.logout()


is_allowed_user(moderator_user)
is_allowed_user(regular_user)
