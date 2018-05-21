"""
This module describes bad examples of Python code.
You should implement a fixed version of each example.
"""

__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"


# Example 1.
strColor = "green"
boolActive = False
intPythonYears = 20
dtPythonFirstUsed = "04/20/2011"

# Example 2.
clr = "green"
ctv = False
pthnYrs = 20
pthnFrstSd = "04/20/2011"

# Example 3.
c = "green"
a = False
p = 20
t = "04/20/2011"

# Your solution should be added here.
# It should be applicable for all 3 examples.
color_in_text = "green"
is_active = False
python_years_old = 20
python_started_date = "04/20/2011"


# Example 4.
def click_button(el):
    return bool(el.click())


try:
    click_button(el)

except NoSuchElementException:
    print("This element not visible")

# Your solution should be added here.
