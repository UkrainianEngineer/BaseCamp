import datetime as dt

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

filename = 'log.txt'

class User:
    def __init__ (self, name, group):
        self.name = name
        self.group = group

    def set_group (self, group_n):
        self.group = group_n

    def check_permissions (self, page_name):
        """Method for check prmissions between group of user and target page. It need only one argument - name of page. Return boolean."""
        self.page_n = page_name.page_t
        if self.group in page_name.allow_list:
            return True
        else:
            return False
            
    def logot(self):
        with open(filename, 'a') as f:
            """Describe..."""
            f.write('\n' + 'User {} has not enough permissions for {} page.'.format(self.name, self.page_n) + str(dt.datetime.now()) + '\n\n')

    def login(self):
        with open(filename, 'a') as f:
            """Describe..."""
            f.write('User {} has been successfully logged in {} page. '.format(self.name, self.page_n) + str(dt.datetime.now()) + '\n\n')
        
   
class Page:
    def __init__ (self, page):
        self.allow_list = []
        self.page_t = page #Name of page for check
                    
    def allow_for (self, allow_list):
        """
        Create allow list.
        """
        for i in allow_list:
            self.allow_list.append(i)
        pass
    

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
    admin_user.logot()
