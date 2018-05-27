"""
This module describes an example of decorator in Python.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


class User:
    pass

current_user = User()
current_user.group = "admin"


def allow_for(allowed_groups):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_group = current_user.group
            # Check if user has one of allowed group.
            if user_group in allowed_groups:
                return func(*args, **kwargs)
            raise Exception("Permission denied.")
        return wrapper
    return decorator


@allow_for(["admin"])
def test_permissions():
    print("This code works only for users with `admin` rights.")

test_permissions()

