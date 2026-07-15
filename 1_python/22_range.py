"""
===========================================================
              RANGE() FUNCTION IN PYTHON
         (Beginner Friendly Explanation)
===========================================================


Definition:
-----------
range() generates a sequence of numbers.

It is mainly used inside loops when we
want to repeat something multiple times.

Syntax:
-------

range(stop)

range(start, stop)

range(start, stop, step)

"""


# ==========================================================
# Example 1 : range(stop)
# ==========================================================

print("========== Example 1 ==========")

for number in range(5):
    print(number)

"""
Output

0
1
2
3
4

Notice:
Python starts from 0
and stops BEFORE 5.
"""


# ==========================================================
# Example 2 : Convert range to List
# ==========================================================

print("\n========== Example 2 ==========")

numbers = list(range(5))

print(numbers)

# Output
# [0, 1, 2, 3, 4]


# ==========================================================
# Example 3 : range(start, stop)
# ==========================================================

print("\n========== Example 3 ==========")

for number in range(3, 8):
    print(number)

"""
Output

3
4
5
6
7
"""


# ==========================================================
# Example 4 : range(start, stop, step)
# ==========================================================

print("\n========== Example 4 ==========")

for number in range(0, 11, 2):
    print(number)

"""
Output

0
2
4
6
8
10

The step is 2.
Python jumps by 2.
"""


# ==========================================================
# Example 5 : Jump by 3
# ==========================================================

print("\n========== Example 5 ==========")

for number in range(1, 20, 3):
    print(number)

"""
Output

1
4
7
10
13
16
19
"""


# ==========================================================
# Example 6 : Countdown
# ==========================================================

print("\n========== Example 6 ==========")

for number in range(10, 0, -1):
    print(number)

print("🚀 Blast Off!")

"""
Output

10
9
8
7
6
5
4
3
2
1
🚀 Blast Off!

Negative step means
count backwards.
"""



# ==========================================================
# Real World Example 4
# ==========================================================

print("\n========== Multiplication Table ==========")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

"""
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""


# ==========================================================
# Real World Example 5
# ==========================================================

print("\n========== ATM PIN Attempts ==========")

for attempt in range(1, 4):
    print(f"Attempt {attempt}")

"""
Most ATM machines allow
only 3 attempts.

range() is perfect for this.
"""


# ==========================================================
# Why Do We Use range()?
# ==========================================================

print("\n========== Why use range()? ==========")

print("""
1. Repeat something many times.

2. Count numbers.

3. Create sequences.

4. Control loops.

5. Access list indexes.

6. Very common in:
   • Games
   • School Systems
   • Banking Software
   • Websites
   • Data Processing
   • Machine Learning
""")


# ==========================================================
# range() with Lists
# ==========================================================

print("\n========== range() with Lists ==========")

fruits = ["Apple", "Mango", "Banana"]

for i in range(len(fruits)):
    print(i, fruits[i])

"""
Output

0 Apple
1 Mango
2 Banana

range(len(list))
gives the indexes.
"""


# ==========================================================
# range() vs enumerate()
# ==========================================================

print("\n========== range() vs enumerate() ==========")

fruits = ["Apple", "Mango", "Banana"]

print("Using range()")

for i in range(len(fruits)):
    print(i, fruits[i])

print("\nUsing enumerate()")

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
Both give the same result.

But enumerate() is cleaner
when you need both index
and value.
"""


# ==========================================================
# range() Memory Efficient
# ==========================================================

print("\n========== Memory Efficient ==========")

numbers = range(1000000)

print(numbers)

"""
Output

range(0, 1000000)

range() does NOT create
1 million numbers immediately.

It generates them only
when needed.

This saves memory.
"""



"""
Easy Rule:

range(stop)
Starts at 0

range(start, stop)
Starts at start

range(start, stop, step)
Moves by step

Always remember:

Python stops BEFORE the stop value.
"""

# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
range() generates a sequence
of numbers.

It is mainly used inside loops
to repeat actions, count numbers,
and work with indexes.
""")