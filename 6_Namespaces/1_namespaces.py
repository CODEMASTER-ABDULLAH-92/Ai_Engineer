# Namespace = WHERE names are stored
# Scope     = WHERE names can be accessed
# LEGB      = HOW Python searches for a name

# =================
# Name Space 
# =================

# A namespace in Python is a place where names are stored and mapped to objects.
# - A namespace keeps track of which name refers to which object.

# Namespace
# ----------------
# name  → "Abdullah"
# age   → 20


# Types of Namespaces
# Python mainly has four important namespaces:


# ===========================
# 1. Built-in Namespace
# ===========================
# Contains Python's built-in names.


# Examples:
print()
len()
str()
int()
list()
Exception()

# Conceptually:

# Built-in Namespace
# ------------------
# print → built-in print function
# len   → built-in len function
# str   → built-in str class
# int   → built-in int class

# It is available throughout your Python program.


# ===========================
# 2. Global Namespace
# ===========================

# Names created at the module/file level.

name = "Abdullah"
age = 20

def hello():
    pass

# The names:
# name
# age
# hello

# belong to the global namespace of that Python file/module.





# ===========================
# 3. Local Namespace
# ===========================
# Names created inside a function.

def calculate():
    x = 10
    y = 20

calculate()


# Here:
# x
# y

# belong to the local namespace of calculate().
# They exist while that function's local scope is active.


# print(x)
# x isn't available globally because it belongs to the function's local namespace.



# =======================
# Enclosing Namespace
# =======================

# This occurs with nested functions.

def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()

# inner() can access x from outer().



# How Python Searches for Names
# Python follows the LEGB rule when looking for a name:

# L → Local
# E → Enclosing
# G → Global
# B → Built-in



# x = "global"

# def outer():
#     x = "enclosing"

#     def inner():
#         x = "local"
#         print(x)

#     inner()

# outer()

# Local
#   ↓
# Enclosing
#   ↓
# Global
#   ↓
# Built-in