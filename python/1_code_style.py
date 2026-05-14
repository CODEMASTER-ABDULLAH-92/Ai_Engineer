"""
PEP 8 COMPLETE GUIDE
====================

PEP 8 = Python Enhancement Proposal 8
It is the official style guide for Python code.


Official Documentation:
https://peps.python.org/pep-0008/
"""
"""
1. Use the snack_case for the variable and function. ==> student_age = 23
2. Use the PascalCase for the ClassName. ==> MyClass
3. Use the Upper Case for the Constant ==> MAX_COUNT
4. Use the proper indentation for the four spaces
5. Use the space around the operators x + y
6. Spaces after commas [1, 2, 3, 4]
7. Imports should usually be on separate lines 
    import math
    import os
8. 2 blank lines for the top level functions and classes and one for the inner methods 
9. Use docstrings for modules, functions, and classes. Like """"""
10.  
"""


# ============================================================
# 1. VARIABLES AND FUNCTION NAMES
# ============================================================

# Use snake_case for variables and functions.

# GOOD
user_name = "Abdullah"
user_age = 20


# GOOD

def calculate_total_price(price, tax):
    return price + tax


# BAD
# userName = "Abdullah"
# UserAge = 20
# def CalculateTotalPrice():
#     pass


# ============================================================
# 2. CLASS NAMES
# ============================================================

# Use PascalCase (CapWords) for classes.


class StudentProfile:
    def __init__(self, name):
        self.name = name


# BAD
# class studentprofile:
#     pass


# ============================================================
# 3. CONSTANTS
# ============================================================

# Constants should be written in UPPER_CASE.

MAX_USERS = 100
PI = 3.14159


# ============================================================
# 4. INDENTATION
# ============================================================

# Use 4 spaces per indentation level.


if user_age > 18:
    print("Adult")


# BAD
# if user_age > 18:
#  print("Adult")


# ============================================================
# 5. SPACES AROUND OPERATORS
# ============================================================

# GOOD
x = 5 + 3


# BAD
# x=5+3


# ============================================================
# 6. SPACES AFTER COMMAS
# ============================================================

# GOOD
numbers = [1, 2, 3, 4]


# BAD
# numbers = [1,2,3,4]


# ============================================================
# 7. LINE LENGTH
# ============================================================

# PEP 8 recommends maximum 79 characters per line.


message = (
    "This is a very long message, so it is split into multiple "
    "lines for better readability."
)


# ============================================================
# 8. IMPORTS
# ============================================================

# Imports should usually be on separate lines.

# GOOD
import math
import os


# BAD
# import math, os


# Standard order:
# 1. Standard library imports
# 2. Third-party imports
# 3. Local imports


# ============================================================
# 9. BLANK LINES
# ============================================================

# Use:
# - 2 blank lines between top-level functions/classes
# - 1 blank line inside class methods


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# ============================================================
# 10. COMMENTS
# ============================================================

# Comments should be clear and meaningful.

# GOOD
# Calculate total salary after bonus.


salary = 50000
bonus = 10000
total_salary = salary + bonus


# BAD
# this adds stuff


# ============================================================
# 11. DOCSTRINGS
# ============================================================

# Use docstrings for modules, functions, and classes.



def multiply(a, b):
    """Return multiplication of two numbers."""
    return a * b


# ============================================================
# 12. BOOLEAN COMPARISONS
# ============================================================

# GOOD
is_logged_in = True

if is_logged_in:
    print("Welcome")


# BAD
# if is_logged_in == True:
#     print("Welcome")


# ============================================================
# 13. NONE COMPARISON
# ============================================================

# Use 'is' instead of '=='.

value = None

if value is None:
    print("Value is None")


# BAD
# if value == None:
#     pass


# ============================================================
# 14. LIST COMPREHENSIONS (PYTHONIC WAY)
# ============================================================

# Pythonic style often prefers concise readable code.

numbers = [1, 2, 3, 4]

# GOOD
squares = [number * number for number in numbers]

print(squares)


# NON-PYTHONIC
# squares = []
# for number in numbers:
#     squares.append(number * number)


# ============================================================
# 15. VARIABLE NAMING BEST PRACTICES
# ============================================================

# GOOD
student_name = "Ali"
total_marks = 90


# BAD
# a = "Ali"
# x = 90


# ============================================================
# 16. AVOID EXTRA WHITESPACE
# ============================================================

# GOOD
result = (x + 5) * 10


# BAD
# result=(x+5)*10


# ============================================================
# 17. TRAILING COMMAS
# ============================================================

# Useful in multiline collections.

languages = [
    "Python",
    "JavaScript",
    "C++",
]


# ============================================================
# 18. EXCEPTION HANDLING
# ============================================================

# Catch specific exceptions.


try:
    number = int("10")
except ValueError:
    print("Invalid number")


# BAD
# except:
#     pass


# ============================================================
# 19. MAIN GUARD
# ============================================================

# Use this when writing executable scripts.



def main():
    print("Program started")


if __name__ == "__main__":
    main()


# ============================================================
# 20. PYTHONIC PRINCIPLES
# ============================================================

# Pythonic code means:
# - Readable
# - Clean
# - Elegant
# - Simple
# - Efficient


# Example

# NON-PYTHONIC
# result = []
# for i in range(10):
#     if i % 2 == 0:
#         result.append(i)


# PYTHONIC
result = [i for i in range(10) if i % 2 == 0]
print(result)



