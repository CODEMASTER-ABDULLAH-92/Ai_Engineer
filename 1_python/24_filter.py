"""
===========================================================
              FILTER() FUNCTION IN PYTHON
         (Beginner Friendly Explanation)
===========================================================

Imagine you have a basket of fruits.

Basket

🍎 Apple
🍌 Banana
🥭 Mango
🍎 Apple
🍇 Grapes

Your mother says,

"Bring me ONLY the Apples."

You remove everything else.

Result

🍎 Apple
🍎 Apple

Python's filter() function works exactly like this.

It keeps only the items that match a condition
and removes everything else.

Definition
----------
filter() selects only those items that satisfy
a condition.

Think of it like a security guard.

People

Ali (18)      ✔ Allowed
Ahmed (12)    ❌ Not Allowed
Sara (20)     ✔ Allowed
Ayesha (15)   ❌ Not Allowed

Only the people who satisfy the rule are allowed.

Syntax
------

filter(function, iterable)

function  -> The condition (rule)

iterable  -> List, Tuple, etc.
"""


# ==========================================================
# Example 1 : Keep Even Numbers
# ==========================================================

print("========== Example 1 ==========")

numbers = [1, 2, 3, 4, 5, 6]


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)

print(list(result))

"""
Output

[2, 4, 6]
"""


# ==========================================================
# Example 2 : Keep Odd Numbers
# ==========================================================

print("\n========== Example 2 ==========")

numbers = [1, 2, 3, 4, 5]


def is_odd(number):
    return number % 2 != 0


result = filter(is_odd, numbers)

print(list(result))

"""
Output

[1, 3, 5]
"""


# ==========================================================
# Example 3 : Keep Adults
# ==========================================================

print("\n========== Example 3 ==========")

ages = [10, 15, 18, 22, 30]


def is_adult(age):
    return age >= 18


result = filter(is_adult, ages)

print(list(result))

"""
Output

[18, 22, 30]
"""


# ==========================================================
# Example 4 : Pass Students
# ==========================================================

print("\n========== Example 4 ==========")

marks = [40, 75, 20, 90, 55]


def passed(mark):
    return mark >= 50


result = filter(passed, marks)

print(list(result))

"""
Output

[75, 90, 55]
"""


# ==========================================================
# Example 5 : Expensive Products
# ==========================================================

print("\n========== Example 5 ==========")

prices = [120, 5, 1000, 20]


def expensive(price):
    return price > 100


result = filter(expensive, prices)

print(list(result))

"""
Output

[120, 1000]
"""


# ==========================================================
# Example 6 : Remove Empty Strings
# ==========================================================

print("\n========== Example 6 ==========")

emails = [
    "ali@gmail.com",
    "",
    "ahmed@gmail.com",
    "",
    "sara@gmail.com"
]

result = filter(bool, emails)

print(list(result))

"""
Output

['ali@gmail.com',
 'ahmed@gmail.com',
 'sara@gmail.com']
"""


# ==========================================================
# Example 7 : Using Lambda
# ==========================================================

print("\n========== Example 7 ==========")

numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x > 20, numbers)

print(list(result))

"""
Output

[25, 30]
"""


# ==========================================================
# Without filter()
# ==========================================================

print("\n========== Without filter() ==========")

numbers = [1, 2, 3, 4, 5, 6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)

print(result)

"""
Output

[2, 4, 6]
"""


# ==========================================================
# With filter()
# ==========================================================

print("\n========== With filter() ==========")

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

"""
Output

[2, 4, 6]

Notice

filter() makes the code
shorter and cleaner.
"""


# ==========================================================
# filter() Returns a Filter Object
# ==========================================================

print("\n========== Filter Object ==========")

numbers = [1, 2, 3]

result = filter(lambda x: x > 1, numbers)

print(result)

"""
Output

<filter object at ...>

filter() returns a filter object.

To see the values,
convert it into a list.
"""

print(list(result))

"""
Output

[2, 3]
"""


# ==========================================================
# Real World Example 1
# ==========================================================

print("\n========== Active Users ==========")

users = [
    {"name": "Ali", "active": True},
    {"name": "Ahmed", "active": False},
    {"name": "Sara", "active": True},
]

active_users = filter(lambda user: user["active"], users)

print(list(active_users))

"""
Imagine a website.

You only want to display
active users.

filter() removes inactive users.
"""


# ==========================================================
# Real World Example 2
# ==========================================================

print("\n========== In Stock Products ==========")

stock = [10, 0, 15, 8, 0, 25]

available = filter(lambda quantity: quantity > 0, stock)

print(list(available))

"""
Products with zero quantity
are removed.
"""


# ==========================================================
# Real World Example 3
# ==========================================================

print("\n========== Adult Movie ==========")

ages = [12, 18, 21, 15, 35]

adults = filter(lambda age: age >= 18, ages)

print(list(adults))

"""
Only adults are allowed
to watch the movie.
"""


# ==========================================================
# Why Do We Use filter()?
# ==========================================================

print("\n========== Why use filter()? ==========")

print("""
1. Remove unwanted data.

2. Keep only useful data.

3. Avoid writing long loops.

4. Make code cleaner.

5. Used in:

   • Login Systems

   • Search Filters

   • E-commerce Websites

   • Banking Software

   • Student Management Systems

   • Data Cleaning

   • Machine Learning

   • APIs

   • Databases
""")


# ==========================================================
# map() vs filter()
# ==========================================================

print("\n========== map() vs filter() ==========")

numbers = [1, 2, 3, 4]

print("Using map()")

result = map(lambda x: x * 2, numbers)

print(list(result))

print("\nUsing filter()")

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

"""
map()

Changes every item.

Result

[2, 4, 6, 8]


filter()

Keeps only matching items.

Result

[2, 4]
"""


# ==========================================================
# Summary
# ==========================================================

print("\n========== Summary ==========")

print("""
Think of filter() as a water filter.

Dirty Water

💧🪨🍂💧🪵💧

↓

Water Filter

↓

Clean Water

💧💧💧

Python does the same.

Data goes in.

Only the data that satisfies
the condition comes out.

Easy Rule

range()      -> Generates numbers.

enumerate() -> Adds indexes.

zip()        -> Joins multiple lists.

map()        -> Changes every item.

filter()     -> Keeps matching items.
""")


# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
filter() applies a condition
to every item in an iterable
and returns only those items
that satisfy the condition.

Think of it as a smart filter
that removes unwanted data.
""")