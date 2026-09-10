# ============================================================
# Operator Overloading in Python
# ============================================================

# Operator overloading means giving operators such as
# +, -, *, ==, <, >, etc. a specific behavior for
# objects of our own class.
#
# It is an important concept of:
#     - Object-Oriented Programming
#     - Polymorphism
#
# Operators:
#
# +     Addition
# -     Subtraction
# *     Multiplication
# /     Division
# ==    Equal to
# <     Less than
# >     Greater than


# ------------------------------------------------------------
# Example
# ------------------------------------------------------------

# Normally:
#
# 10 + 20
#
# gives:
#
# 30
#
# But:
#
# "Hello" + "World"
#
# gives:
#
# "HelloWorld"
#
# The same + operator behaves differently depending
# on the objects being used.


# ------------------------------------------------------------
# Operator Overloading with a Class
# ------------------------------------------------------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __add__() defines the behavior of +
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


p1 = Point(10, 20)
p2 = Point(5, 10)

p3 = p1 + p2

print(p3.x)    # 15
print(p3.y)    # 30


# ------------------------------------------------------------
# What happens internally?
# ------------------------------------------------------------

# When Python sees:
#
# p1 + p2
#
# it essentially calls:
#
# p1.__add__(p2)
#
# Therefore:
#
# + operator
#      ↓
# __add__() method
#      ↓
# Our custom behavior


# ------------------------------------------------------------
# Common Operator Overloading Methods
# ------------------------------------------------------------

# +     → __add__()
# -     → __sub__()
# *     → __mul__()
# /     → __truediv__()
# //    → __floordiv__()
# %     → __mod__()
# **    → __pow__()
# ==    → __eq__()
# !=    → __ne__()
# <     → __lt__()
# >     → __gt__()
# <=    → __le__()
# >=    → __ge__()


# ============================================================
# Key Definition
# ============================================================

# Operator Overloading:
#
# "Defining how an operator behaves when it is used
# with objects of our own class."
#
# Example:
#
# object1 + object2
#
# can be customized using:
#
# __add__()
# ============================================================