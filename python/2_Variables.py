"""
Python Variables - Complete Beginner Guide
"""

# ==========================================
# What is a Variable?
# ==========================================
# A variable is used to store data in memory.

name = "Abdullah"
age = 20
price = 99.9

print("Name:", name)
print("Age:", age)
print("Price:", price)


# ==========================================
# Rules for Variable Names
# ==========================================

# Valid variable names
user_name = "Ali"
age2 = 21
_marks = 90

print(user_name)
print(age2)
print(_marks)

# Invalid variable names (commented because they cause errors)
# 2age = 20
# user-name = ""
# class = "A"


# ==========================================
# Multiple Variables
# ==========================================

# Assign multiple values

a, b, c = 1, 2, 3
print(a, b, c)

# Same value to multiple variables
x = y = z = 100
print(x, y, z)


# ==========================================
# Updating Variables
# ==========================================

count = 1
count = count + 1

print("Updated Count:", count)

# Shortcut method
count += 1
print("Shortcut Updated Count:", count)


# ==========================================
# Printing Variables
# ==========================================

name = "Abdullah"
print(name)


# ==========================================
# Checking Variable Type
# ==========================================

age = 20
print(type(age))

