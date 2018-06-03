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
    
    def __init__(self, user_name, role):
        self.user_name = user_name
        self.role = role

    def set_group(self, new_role):
        self.role = new_role

    def check_permissions(self, current_page):
        global used_page
        used_page = current_page.page_name
        if self.role in current_page.allowed_role:
            return True
    
    def login(self):
            log_info = 'User {} has been successfully logged in {} page.'.format(self.user_name, used_page)
            self.wright_log_info(log_info)
        
    def logout(self):
        log_info = 'User {} has not enough permissions for {} page.'.format(self.user_name, used_page)
        self.wright_log_info(log_info)

    def wright_log_info(self, message):
        with open('Activity log', 'w') as a_file:
            a_file.write(message)
        

class Page:
    def __init__(self, page_name):
        self.page_name = page_name
        
    allowed_role = []
    
    def allow_for(self, *args):
        for i in args:
            if i not in self.allowed_role:
                self.allowed_role += i

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
