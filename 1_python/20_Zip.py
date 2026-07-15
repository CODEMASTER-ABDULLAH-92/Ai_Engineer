"""
===========================================================
            ZIP() FUNCTION IN PYTHON
          (Beginner Friendly Explanation)
===========================================================

Imagine you have a jacket.

The jacket has two sides:

Left Side               Right Side
---------               ----------
Ali                     Apple
Ahmed                   Mango
Sara                    Banana

When you close the zipper, each item on the left joins with
the matching item on the right.

Result:

(Ali, Apple)
(Ahmed, Mango)
(Sara, Banana)

Python's zip() function works exactly the same way.

Definition:
-----------
zip() combines two or more lists (or other iterables)
item by item.

zip() takes two or more sequences (like lists or tuples) and combines their items into matching pairs (or groups), one position at a time.
Syntax:
-------
zip(list1, list2)

"""


# ==========================================================
# Example 1 : Basic Example
# ==========================================================

print("========== Example 1 ==========")

names = ["Ali", "Ahmed", "Sara"]
fruits = ["Apple", "Mango", "Banana"]

result = zip(names, fruits)

print(list(result))

# Output:
# [('Ali', 'Apple'), ('Ahmed', 'Mango'), ('Sara', 'Banana')]


# ==========================================================
# Example 2 : Using a for loop
# ==========================================================

print("\n========== Example 2 ==========")

names = ["Ali", "Ahmed", "Sara"]
fruits = ["Apple", "Mango", "Banana"]

for name, fruit in zip(names, fruits):
    print(name, "likes", fruit)

# Output:
# Ali likes Apple
# Ahmed likes Mango
# Sara likes Banana


# ==========================================================
# Example 3 : Students and Marks
# ==========================================================

print("\n========== Example 3 ==========")

students = ["A", "B", "C"]
marks = [90, 80, 70]

for student, mark in zip(students, marks):
    print(student, "got", mark)

# Output:
# A got 90
# B got 80
# C got 70


# ==========================================================
# Example 4 : Products and Prices
# ==========================================================

print("\n========== Example 4 ==========")

products = ["Laptop", "Mouse", "Keyboard"]
prices = [1000, 20, 50]

for product, price in zip(products, prices):
    print(product, "=", "$" + str(price))

# Output:
# Laptop = $1000
# Mouse = $20
# Keyboard = $50


# ==========================================================
# Example 5 : Three Lists
# ==========================================================

print("\n========== Example 5 ==========")

names = ["Ali", "Ahmed"]
ages = [20, 22]
cities = ["Lahore", "Karachi"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)

# Output:
# Ali 20 Lahore
# Ahmed 22 Karachi


# ==========================================================
# Example 6 : Different Length Lists
# ==========================================================

print("\n========== Example 6 ==========")

names = ["Ali", "Ahmed", "Sara"]
marks = [95, 88]

print(list(zip(names, marks)))

# Output:
# [('Ali', 95), ('Ahmed', 88)]

"""
Notice:

Sara is ignored.

Why?

Because zip() stops when the shortest iterable ends.
"""


# ==========================================================
# Without zip()
# ==========================================================

print("\n========== Without zip() ==========")

students = ["A", "B", "C"]
marks = [90, 80, 70]

for i in range(len(students)):
    print(students[i], marks[i])


# ==========================================================
# With zip()
# ==========================================================

print("\n========== With zip() ==========")

for student, mark in zip(students, marks):
    print(student, mark)

"""
The zip() version is:
✔ Shorter
✔ Cleaner
✔ Easier to read
"""


# ==========================================================
# Real World Example
# ==========================================================

print("\n========== Real World Example ==========")

usernames = ["abdullah", "ali", "ahmed"]
emails = [
    "abdullah@gmail.com",
    "ali@gmail.com",
    "ahmed@gmail.com"
]

for username, email in zip(usernames, emails):
    print(f"Sending email to {username} at {email}")

"""
Imagine you're building a website.

The database gives you:

Names:
------
Ali
Ahmed
Sara

Emails:
-------
ali@gmail.com
ahmed@gmail.com
sara@gmail.com

Instead of matching them manually, zip() pairs them
automatically.
"""


# ==========================================================
# Why do we use zip()?
# ==========================================================

print("\n========== Why use zip()? ==========")

print("""
1. Combines related data together.

2. Makes code shorter.

3. Makes code easier to read.

4. Avoids using indexes.

5. Very useful in:
   • Student Management Systems
   • E-commerce Websites
   • Employee Records
   • APIs
   • Database Applications
   • Data Analysis
""")


# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
zip() combines two or more iterables
(list, tuple, etc.) by pairing their
elements position by position.

Think of a jacket zipper:

Left Side        Right Side

Ali              Apple
Ahmed            Mango
Sara             Banana

        ↓ zip()

(Ali, Apple)
(Ahmed, Mango)
(Sara, Banana)

That's why the function is called zip().
""")








