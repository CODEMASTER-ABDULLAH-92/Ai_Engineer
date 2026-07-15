"""
===========================================================
               MAP() FUNCTION IN PYTHON
         (Beginner Friendly Explanation)
===========================================================

# map() applies a function to every item in an iterable (like a list) and returns the transformed values.

# syntax 
# map(function, iterable)


Imagine you are a teacher.

Students' Marks

10
20
30
40
50

The principal says:

"Add 5 bonus marks to EVERY student."

Instead of adding 5 one by one,

10 -> 15
20 -> 25
30 -> 35
40 -> 45
50 -> 55

Python's map() function does this automatically.

Definition:
-----------
map() applies the SAME function to EVERY item
in a list (or other iterable).

Think of it like a machine.

10 ---> +5 ---> 15

20 ---> +5 ---> 25

30 ---> +5 ---> 35

40 ---> +5 ---> 45

50 ---> +5 ---> 55

Every item goes through the same machine.

Syntax:
-------

map(function, iterable)

function  -> What should happen to each item?

iterable  -> List, Tuple, etc.
"""


# ==========================================================
# Example 1 : Add 5 to Every Number
# ==========================================================

print("========== Example 1 ==========")

numbers = [10, 20, 30, 40]


def add_five(num):
    return num + 5


result = map(add_five, numbers)

print(list(result))

"""
Output

[15, 25, 35, 45]
"""


# ==========================================================
# Example 2 : Square Every Number
# ==========================================================

print("\n========== Example 2 ==========")

numbers = [1, 2, 3, 4, 5]


def square(number):
    return number * number


result = map(square, numbers)

print(list(result))

"""
Output

[1, 4, 9, 16, 25]
"""


# ==========================================================
# Example 3 : Double Every Number
# ==========================================================

print("\n========== Example 3 ==========")

numbers = [2, 4, 6, 8]

result = map(lambda x: x * 2, numbers)

print(list(result))

"""
Output

[4, 8, 12, 16]
"""


# ==========================================================
# Example 4 : Convert Names to Uppercase
# ==========================================================

print("\n========== Example 4 ==========")

names = ["ali", "ahmed", "sara"]

result = map(str.upper, names)

print(list(result))

# 2nd Method 


result = map((lambda name: name.upper()), names)
print("2nd Method: ",list(result))

"""
Output

['ALI', 'AHMED', 'SARA']
"""


# ==========================================================
# Example 5 : Convert Celsius to Fahrenheit
# ==========================================================

print("\n========== Example 5 ==========")

temperatures = [20, 25, 30]


def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


result = map(to_fahrenheit, temperatures)

print(list(result))

"""
Output

[68.0, 77.0, 86.0]
"""


# ==========================================================
# Real World Example 1
# ==========================================================

print("\n========== Product Discount ==========")

prices = [100, 200, 300, 400]


def discount(price):
    return price * 0.90


discounted_prices = map(discount, prices)

print(list(discounted_prices))

"""
Imagine an online shopping website.

Every product gets a 10% discount.

Instead of updating prices one by one,
map() updates all prices automatically.
"""


# ==========================================================
# Real World Example 2
# ==========================================================

print("\n========== Student Bonus Marks ==========")

marks = [70, 80, 90]


def bonus(mark):
    return mark + 5


new_marks = map(bonus, marks)

print(list(new_marks))

"""
Every student receives
5 bonus marks.
"""


# ==========================================================
# Real World Example 3
# ==========================================================

print("\n========== Salary Increase ==========")

salaries = [50000, 60000, 70000]


def increase_salary(salary):
    return salary * 1.10


new_salaries = map(increase_salary, salaries)

print(list(new_salaries))

"""
Companies often increase
every employee's salary
by the same percentage.

map() is perfect for this.
"""


# ==========================================================
# Without map()
# ==========================================================

print("\n========== Without map() ==========")

numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(number * 2)

print(result)

"""
Output

[2, 4, 6, 8]
"""


# ==========================================================
# With map()
# ==========================================================

print("\n========== With map() ==========")

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

"""
Output

[2, 4, 6, 8]

Notice:

map() is shorter
and cleaner.
"""


# ==========================================================
# map() Returns a Map Object
# ==========================================================

print("\n========== Map Object ==========")

numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)

"""
Output

<map object at ...>

To see the values,
convert it into a list.
"""

print(list(result))

"""
Output

[2, 4, 6]
"""


# ==========================================================
# Why Do We Use map()?
# ==========================================================

print("\n========== Why use map()? ==========")

print("""
1. Apply the same operation
   to every item.

2. Make code shorter.

3. Avoid writing loops.

4. Improve readability.

5. Very useful in:

   • Data Analysis

   • Machine Learning

   • Web Development

   • APIs

   • Databases

   • Data Cleaning

   • Currency Conversion

   • Temperature Conversion

   • Discounts

   • Salary Calculations
""")


# ==========================================================
# map() vs for Loop
# ==========================================================

print("\n========== map() vs for Loop ==========")

numbers = [1, 2, 3, 4]

print("Using for loop")

result = []

for number in numbers:
    result.append(number * 2)

print(result)

print("\nUsing map()")

result = map(lambda x: x * 2, numbers)

print(list(result))

"""
Both produce the same result.

But map() is shorter
for simple transformations.
"""


# ==========================================================
# Summary
# ==========================================================

print("\n========== Summary ==========")

print("""
Think of map() as a machine.

Every item enters the machine.

The machine performs
the SAME operation
on every item.

Example

10

↓

+5

↓

15

20

↓

+5

↓

25

30

↓

+5

↓

35

This is exactly how map() works.

Easy Rule

range()      -> Generates numbers.

enumerate() -> Adds index.

zip()        -> Joins multiple lists.

map()        -> Changes every item.
""")


# ==========================================================
# One-Line Definition
# ==========================================================

print("\n========== Definition ==========")

print("""
map() applies the same function
to every item in an iterable
and returns the transformed values.

Think of it as a machine that
processes every item
in exactly the same way.
""")