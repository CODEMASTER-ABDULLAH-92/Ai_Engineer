"""
===========================================================
            ENUMERATE() FUNCTION IN PYTHON
         (Beginner Friendly Explanation)
===========================================================

Imagine you are a teacher.

Students:

Ali
Ahmed
Sara

You want to give every student a roll number.

1 → Ali
2 → Ahmed
3 → Sara

Python's enumerate() function does exactly this.

It gives every item a number (called an index).

Definition:
-----------
enumerate() adds a number (index) to every item
while looping through a list (or any iterable).

Syntax:
-------
enumerate(iterable)

or

enumerate(iterable, start=1)
"""


# ==========================================================
# Example 1 : Basic Example
# ==========================================================

print("========== Example 1 ==========")

names = ["Ali", "Ahmed", "Sara"]

for item in enumerate(names):
    print(item)

# Output:
# (0, 'Ali')
# (1, 'Ahmed')
# (2, 'Sara')


# ==========================================================
# Example 2 : Getting Index and Value
# ==========================================================

print("\n========== Example 2 ==========")

names = ["Ali", "Ahmed", "Sara"]

for index, name in enumerate(names):
    print(index, name)

# Output:
# 0 Ali
# 1 Ahmed
# 2 Sara


# ==========================================================
# Example 3 : Start Counting from 1
# ==========================================================

print("\n========== Example 3 ==========")

students = ["Ali", "Ahmed", "Sara"]

for roll_no, student in enumerate(students, start=1):
    print(roll_no, student)

# Output:
# 1 Ali
# 2 Ahmed
# 3 Sara


# ==========================================================
# Example 4 : Shopping Cart
# ==========================================================

print("\n========== Example 4 ==========")

cart = ["Laptop", "Mouse", "Keyboard"]

for number, item in enumerate(cart, start=1):
    print(number, item)

# Output:
# 1 Laptop
# 2 Mouse
# 3 Keyboard


# ==========================================================
# Example 5 : Playlist
# ==========================================================

print("\n========== Example 5 ==========")

songs = ["Believer", "Shape of You", "Perfect"]

for number, song in enumerate(songs, start=1):
    print(number, song)

# Output:
# 1 Believer
# 2 Shape of You
# 3 Perfect


# ==========================================================
# Without enumerate()
# ==========================================================

print("\n========== Without enumerate() ==========")

books = ["Python", "Java", "C++"]

for i in range(len(books)):
    print(i, books[i])

"""
Output:
0 Python
1 Java
2 C++
"""


# ==========================================================
# With enumerate()
# ==========================================================

print("\n========== With enumerate() ==========")

books = ["Python", "Java", "C++"]

for index, book in enumerate(books):
    print(index, book)

"""
Output:
0 Python
1 Java
2 C++
"""

print("""
Notice:

Both examples produce the same result.

But enumerate() is:
✔ Shorter
✔ Cleaner
✔ Easier to read
✔ Preferred by Python programmers
""")


# ==========================================================
# Real World Example 1
# ==========================================================

print("\n========== Student Attendance ==========")

students = ["Ali", "Ahmed", "Sara", "Ayesha"]

for roll_no, student in enumerate(students, start=1):
    print(f"Roll No {roll_no}: {student}")

"""
Imagine a school attendance system.

Instead of writing roll numbers manually,
enumerate() generates them automatically.
"""


# ==========================================================
# Real World Example 2
# ==========================================================

print("\n========== To-Do List ==========")

tasks = [
    "Wake up",
    "Study Python",
    "Complete Homework",
    "Go to Gym"
]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

"""
Almost every To-Do app numbers tasks like this.
"""


# ==========================================================
# Real World Example 3
# ==========================================================

print("\n========== Leaderboard ==========")

players = ["Ali", "Ahmed", "Sara"]

for rank, player in enumerate(players, start=1):
    print(f"Rank {rank}: {player}")

"""
Games use enumerate() to display rankings.
"""


# ==========================================================
# Why Do We Use enumerate()?
# ==========================================================

print("\n========== Why use enumerate()? ==========")

print("""
1. Gives every item a number.

2. Makes code cleaner.

3. Avoids using range(len()).

4. Makes programs easier to read.

5. Used in:
   • Student Attendance Systems
   • Shopping Carts
   • Leaderboards
   • Quiz Apps
   • To-Do Lists
   • Playlists
   • Numbered Menus
   • Data Processing
""")


# ==========================================================
# enumerate() vs range(len())
# ==========================================================

print("\n========== enumerate() vs range(len()) ==========")

fruits = ["Apple", "Mango", "Banana"]

print("Using range(len())")

for i in range(len(fruits)):
    print(i, fruits[i])

print("\nUsing enumerate()")

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
enumerate() adds an index (number)
to every item in a list or other iterable.

Think of it like giving every student
a roll number.

Students

Ali
Ahmed
Sara

↓

After enumerate()

0 → Ali
1 → Ahmed
2 → Sara

or

1 → Ali
2 → Ahmed
3 → Sara

(using start=1)

That's why enumerate() is used whenever
you need BOTH the position and the value
while looping.
""")