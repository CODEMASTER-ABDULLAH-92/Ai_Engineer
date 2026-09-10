# ============================================================
# Magic Methods in Python
# ============================================================

# Magic methods are special methods in Python.
#
# They start and end with double underscores:
#
#     __method__()
#
# They are also called:
#
#   Dunder Methods
#
# Dunder = Double Underscore


# ------------------------------------------------------------
# __init__()
# ------------------------------------------------------------

# __init__() is automatically called when an object
# is created.
#
# It is commonly used to initialize object attributes.


class Student:

    def __init__(self, name):
        self.name = name


student = Student("Ali")


# ------------------------------------------------------------
# __str__()
# ------------------------------------------------------------

# __str__() controls what is displayed when
# print(object) is used.


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


person = Person("Ali")

print(person)

# Output:
# Person: Ali


# ------------------------------------------------------------
# __add__()
# ------------------------------------------------------------

# __add__() defines the behavior of the + operator.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )


p1 = Point(10, 5)
p2 = Point(10, 15)

p3 = p1 + p2

# Python internally uses:
#
# p1.__add__(p2)


# ------------------------------------------------------------
# __len__()
# ------------------------------------------------------------

# __len__() defines what happens when
# len(object) is used.


class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Ali", "Ahmed", "Usman"])

print(len(team))

# Output:
# 3


# ------------------------------------------------------------
# Common Magic Methods
# ------------------------------------------------------------

# __init__()      → Initialize an object
# __str__()       → String representation
# __repr__()      → Developer representation
# __add__()       → +
# __sub__()       → -
# __mul__()       → *
# __truediv__()   → /
# __eq__()        → ==
# __lt__()        → <
# __gt__()        → >
# __len__()       → len()
# __getitem__()   → object[index]
# __setitem__()   → object[index] = value


# ============================================================
# Magic Methods + Operator Overloading
# ============================================================

# Operator overloading is commonly implemented
# using magic methods.
#
# Examples:
#
# p1 + p2
#     ↓
# __add__()
#
# p1 - p2
#     ↓
# __sub__()
#
# p1 == p2
#     ↓
# __eq__()
#
# len(p1)
#     ↓
# __len__()
#
# print(p1)
#     ↓
# __str__()


# ============================================================
# Key Definition
# ============================================================

# Magic Methods:
#
# "Special methods with double underscores that allow
# Python objects to interact with built-in operations
# and Python syntax."
# ============================================================