"""
===========================================================
              REDUCE() FUNCTION IN PYTHON
         (Beginner Friendly Explanation)
===========================================================

Imagine you have money.

10
20
30
40

Instead of keeping all numbers separately,

You want ONE answer.

10 + 20 + 30 + 40

↓

100

This is exactly what reduce() does.

Definition
----------

reduce() combines all values into
one final value.

Unlike map() and filter(),

reduce() is imported from functools.

from functools import reduce

Syntax

reduce(function, iterable)
"""

from functools import reduce


# ==========================================================
# Example 1 : Sum of Numbers
# ==========================================================

print("========== Example 1 ==========")

numbers = [10, 20, 30, 40]


def add(x, y):
    return x + y


result = reduce(add, numbers)

print(result)

"""
Output

100
"""


# ==========================================================
# Example 2 : Multiply Numbers
# ==========================================================

print("\n========== Example 2 ==========")

numbers = [2, 3, 4]


def multiply(x, y):
    return x * y


result = reduce(multiply, numbers)

print(result)

"""
Output

24
"""


# ==========================================================
# Example 3 : Find Maximum Number
# ==========================================================

print("\n========== Example 3 ==========")

numbers = [15, 90, 45, 12]


def maximum(x, y):
    if x > y:
        return x
    return y


result = reduce(maximum, numbers)

print(result)

"""
Output

90
"""


# ==========================================================
# Example 4 : Using Lambda
# ==========================================================

print("\n========== Example 4 ==========")

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

"""
Output

15
"""


# ==========================================================
# Real World Example 1
# ==========================================================

print("\n========== Shopping Cart ==========")

prices = [100, 200, 300, 400]

total = reduce(lambda x, y: x + y, prices)

print("Total Bill =", total)

"""
Imagine an online shopping website.

Every product price is added together.

100

+

200

+

300

+

400

↓

1000
"""


# ==========================================================
# Real World Example 2
# ==========================================================

print("\n========== Student Marks ==========")

marks = [80, 90, 70, 60]

total_marks = reduce(lambda x, y: x + y, marks)

print(total_marks)

"""
Total Marks

300
"""


# ==========================================================
# Real World Example 3
# ==========================================================

print("\n========== Company Revenue ==========")

monthly_sales = [12000, 18000, 25000, 15000]

year_sales = reduce(lambda x, y: x + y, monthly_sales)

print(year_sales)

"""
Total Revenue

70000
"""


# ==========================================================
# Without reduce()
# ==========================================================

print("\n========== Without reduce() ==========")

numbers = [1, 2, 3, 4]

total = 0

for number in numbers:
    total += number

print(total)


# ==========================================================
# With reduce()
# ==========================================================

print("\n========== With reduce() ==========")

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)

print(total)

"""
Both produce the same answer.

reduce() is shorter.
"""


# ==========================================================
# Why Do We Use reduce()?
# ==========================================================

print("\n========== Why use reduce()? ==========")

print("""
1. Find total sum.

2. Multiply values.

3. Find maximum.

4. Find minimum.

5. Combine data into one value.

6. Used in:

   • Shopping Cart

   • Banking

   • Finance

   • Data Analysis

   • Machine Learning

   • Statistics

   • Reports

   • Revenue Calculation
""")


# ==========================================================
# Summary
# ==========================================================

print("\n========== Summary ==========")

print("""
Think of reduce() as a combining machine.

10

20

30

40

↓

10 + 20

↓

30

↓

30 + 30

↓

60

↓

60 + 40

↓

100

One final value remains.

Easy Rule

range()      -> Generates numbers.

enumerate() -> Adds index.

zip()        -> Joins lists.

map()        -> Changes every item.

filter()     -> Removes unwanted items.

reduce()     -> Combines everything into ONE value.
""")


# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
reduce() repeatedly applies
a function to combine all items
of an iterable into a single value.

Think of it as reducing
many values into one final result.
""")