"""
===============================================================
          MUTABLE vs IMMUTABLE IN PYTHON
         (Complete Beginner Friendly Guide)
===============================================================

Imagine you have TWO toys.

Toy 1

Clay 🧱

You can change it into

😊

🚗

🏠

Again and again.

This is called

MUTABLE

---------------------------------------------------------------

Toy 2

A Glass Cup 🥛

Once it is made,

you cannot reshape it.

If you want another cup,

you must create a NEW one.

This is called

IMMUTABLE

---------------------------------------------------------------

Definition

Mutable
--------

An object that CAN be changed
after it is created.

Immutable
----------

An object that CANNOT be changed
after it is created.

"""


# ===============================================================
# Mutable Example
# ===============================================================

print("============== Mutable Example ==============")

numbers = [1, 2, 3]

print("Before :", numbers)

numbers.append(4)

print("After  :", numbers)

"""
Output

Before : [1, 2, 3]

After  : [1, 2, 3, 4]

The SAME list changed.
"""


# ===============================================================
# Immutable Example
# ===============================================================

print("\n============== Immutable Example ==============")

name = "Ali"

print("Before :", name)

name = "Ahmed"

print("After  :", name)

"""
Output

Before : Ali

After  : Ahmed

Did Python change "Ali"?

NO

Python created a NEW string.

Strings cannot be modified.
"""


# ===============================================================
# Memory Address (Mutable)
# ===============================================================

print("\n============== Mutable Memory ==============")

numbers = [10, 20, 30]

print("Before ID :", id(numbers))

numbers.append(40)

print("After ID  :", id(numbers))

"""
Output

Same ID

Why?

Because the SAME object changed.
"""


# ===============================================================
# Memory Address (Immutable)
# ===============================================================

print("\n============== Immutable Memory ==============")

text = "Python"

print("Before ID :", id(text))

text = "Java"

print("After ID  :", id(text))

"""
Output

Different IDs

Why?

A NEW string object was created.
"""


# ===============================================================
# Mutable Objects
# ===============================================================

print("\n============== Mutable Objects ==============")

print("""

List
Dictionary
Set
These objects can be changed.

""")


# ===============================================================
# Immutable Objects
# ===============================================================

print("\n============== Immutable Objects ==============")

print("""
Integer
Float
Boolean
String
Tuple
These objects cannot be changed.

""")



# ===============================================================
# Assignment With Mutable Object
# ===============================================================

print("\n============== Assignment With List ==============")

a = [1, 2, 3]

b = a

b.append(4)

print("a =", a)

print("b =", b)

"""
Output

a = [1,2,3,4]

b = [1,2,3,4]

Why?

Both variables refer
to the SAME list.
"""


# ===============================================================
# Assignment With Immutable Object
# ===============================================================

print("\n============== Assignment With String ==============")

a = "Ali"

b = a

b = "Ahmed"

print("a =", a)

print("b =", b)

"""
Output

a = Ali

b = Ahmed

Strings are Immutable.

Changing b creates
a NEW string.

a stays unchanged.
"""


# ===============================================================
# Mutable vs Shallow Copy
# ===============================================================

import copy

print("\n============== Mutable + Shallow Copy ==============")

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

copied[0].append(100)

print(original)

print(copied)

"""
Output

[[1,2,100],[3,4]]

[[1,2,100],[3,4]]

Why?

Inner lists are Mutable.

Both variables share
the same inner list.
"""


# ===============================================================
# Immutable + Shallow Copy
# ===============================================================

print("\n============== Immutable + Shallow Copy ==============")

original = [1, 2, 3]

copied = copy.copy(original)

copied[0] = 100

print(original)

print(copied)

"""
Output

[1,2,3]

[100,2,3]

Integers are Immutable.

Replacing one integer
does not affect
the original list.
"""


# ===============================================================
# Easy Trick
# ===============================================================

print("\n============== Easy Trick ==============")

print("""

Mutable

M

↓

Modify




Immutable

Impossible
to Modify

""")
