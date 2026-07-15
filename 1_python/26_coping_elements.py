# A shallow copy always copies the references of the elements. The shared-reference behavior becomes noticeable only when those elements are mutable objects (like lists, dictionaries, or sets), which are often nested inside another container.


# IF the elements are nested then it copies the reference 

#====================================================
# Case 1: Flat list (immutable elements)
#====================================================

import copy

original = [1, 2, 3]
copied = copy.copy(original)

copied[0] = 100

print(original)  # [1, 2, 3]
print(copied)    # [100, 2, 3]

# Why?

# The outer list is copied.
# Integers (1, 2, 3) are immutable.
# copied[0] = 100 changes the copied list to point to a different integer.
# The original list is unaffected.





# ============================================
# Case 2: Nested list (mutable elements)
# ============================================

import copy

original = [[1,2], [3,4]]

copied = copy.copy(original) 

# copied[0] = 100 # This is not change the reference because it does not modify the list 

# print(original)
# print(copied)


copied[0].append(100)
print(original)
print(copied)















"""
===============================================================
          SHALLOW COPY vs DEEP COPY IN PYTHON
        (Complete Beginner Friendly Guide)
===============================================================

Imagine you have a school bag.

Inside your bag are two pencil boxes.

Bag
│
├── Pencil Box 1
│      ✏️ Pencil
│      🖊️ Pen
│
└── Pencil Box 2
       📏 Ruler
       📚 Eraser

Now your friend wants a copy of your bag.

There are TWO ways to copy it.

1. Shallow Copy
2. Deep Copy

Let's understand both.

"""

import copy


# ===============================================================
# PART 1
# Assignment (=)
# ===============================================================

print("============== Assignment (=) ==============")

original = [1, 2, 3]

copied = original

copied[0] = 100

print("Original :", original)
print("Copied   :", copied)

"""
Output

Original : [100, 2, 3]
Copied   : [100, 2, 3]

Why?

Because copied is NOT a copy.

Both variables point to
the EXACT SAME list.

Memory

original
    │
    ▼
[1,2,3]

copied
    │
    └──────────────► SAME LIST
"""


# ===============================================================
# PART 2
# Shallow Copy
# ===============================================================

print("\n============== Shallow Copy ==============")

original = [1, 2, 3]

copied = copy.copy(original)

copied[0] = 100

print("Original :", original)
print("Copied   :", copied)

"""
Output

Original : [1,2,3]
Copied   : [100,2,3]

Why?

copy.copy() creates a NEW OUTER LIST.

The two lists are different.

Memory

original

[1,2,3]

copied

[100,2,3]

Notice

Changing copied
does NOT affect original.
"""


# ===============================================================
# Check Memory
# ===============================================================

print("\n============== Different Objects ==============")

original = [1, 2, 3]

copied = copy.copy(original)

print(original is copied)

"""
Output

False

They are two different lists.
"""


# ===============================================================
# IMPORTANT
# ===============================================================

print("\n============== Important ==============")

"""
Many beginners think

Shallow Copy always changes
the original.

THIS IS WRONG.

It ONLY happens with
nested mutable objects.
"""


# ===============================================================
# PART 3
# Nested List
# ===============================================================

print("\n============== Nested List ==============")

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

print(original)
print(copied)

"""
Both look identical.

But...

The OUTER LIST is copied.

The INNER LISTS are SHARED.
"""


# ===============================================================
# Check References
# ===============================================================

print("\n============== Shared Inner Lists ==============")

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

print(original is copied)

print(original[0] is copied[0])

print(original[1] is copied[1])

"""
Output

False

True

True

Outer list

Different

Inner lists

Shared
"""


# ===============================================================
# Modify Inner List
# ===============================================================

print("\n============== Modify Inner List ==============")

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

append()

MODIFIES

the SAME inner list.

Both point to it.

Memory

original

│

├────► [1,2,100]

└────► [3,4]


copied

│

├────► [1,2,100]

└────► [3,4]
"""


# ===============================================================
# Replace Inner List
# ===============================================================

print("\n============== Replace Inner List ==============")

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

copied[0] = [100]

print(original)

print(copied)

"""
Output

[[1,2],[3,4]]

[[100],[3,4]]

Why?

You DID NOT modify

[1,2]

Instead

You replaced

copied[0]

with a BRAND NEW LIST.

Memory

original

│

├────► [1,2]

└────► [3,4]


copied

│

├────► [100]

└────► [3,4]
"""


# ===============================================================
# Replace With Integer
# ===============================================================

print("\n============== Replace With Integer ==============")

original = [[1, 2], [3, 4]]

copied = copy.copy(original)

copied[0] = 100

print(original)

print(copied)

"""
Output

[[1,2],[3,4]]

[100,[3,4]]

Again

You replaced the REFERENCE.

You DID NOT modify

[1,2]

Therefore

Original stays unchanged.
"""


# ===============================================================
# PART 4
# Deep Copy
# ===============================================================

print("\n============== Deep Copy ==============")

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

print(original)

print(copied)

"""
Deep Copy copies

Everything.

Outer list

Inner list

Every nested object.
"""


# ===============================================================
# Different References
# ===============================================================

print("\n============== Deep Copy References ==============")

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

print(original is copied)

print(original[0] is copied[0])

print(original[1] is copied[1])

"""
Output

False

False

False

Nothing is shared.
"""


# ===============================================================
# Modify Deep Copy
# ===============================================================

print("\n============== Modify Deep Copy ==============")

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

copied[0].append(100)

print(original)

print(copied)

"""
Output

Original

[[1,2],[3,4]]

Copied

[[1,2,100],[3,4]]

Original never changes.

Why?

Because copied has
its OWN inner lists.
"""


# ===============================================================
# Real Life Example
# ===============================================================

print("\n============== Real Life Example ==============")

"""
Imagine Google Drive.

Projects

│

├── Python

├── Java

└── Images

Shallow Copy

Copies only the folder.

Files are shared.

Editing a file changes both folders.

Deep Copy

Copies

Folder

Every subfolder

Every file

Now editing one folder
does not affect the other.
"""


# ===============================================================
# Assignment vs Shallow vs Deep
# ===============================================================

print("\n============== Comparison ==============")

print("""

Assignment (=)

One object

Two variable names


Shallow Copy

New outer object

Inner mutable objects shared


Deep Copy

Everything copied

Nothing shared

""")


# ===============================================================
# When To Use What?
# ===============================================================

print("\n============== When To Use ==============")

print("""

Assignment

When you want both variables
to refer to the SAME object.


Shallow Copy

When only the outer container
needs to be copied and
sharing nested objects is acceptable.


Deep Copy

When you need a completely
independent copy and do NOT
want changes to affect the original.

""")


# ===============================================================
# Interview Questions
# ===============================================================

print("\n============== Common Interview Questions ==============")

print("""

Q1.

Does shallow copy create a new object?

YES.

Only the OUTER object.


Q2.

Does shallow copy copy nested lists?

NO.

It copies only their references.


Q3.

When does shallow copy become confusing?

When nested mutable objects
like lists, dictionaries,
or sets exist.


Q4.

Does deep copy copy nested objects?

YES.

Everything.


Q5.

Which one uses more memory?

Deep Copy.


Q6.

Which one is faster?

Shallow Copy.

""")


# ===============================================================
# Easy Rules
# ===============================================================

print("\n============== Easy Rules ==============")

print("""

Assignment

One object.

No copy.


Shallow Copy

New outer object.

Shared inner mutable objects.


Deep Copy

Everything is copied.

Nothing is shared.

""")


# ===============================================================
# Final Summary
# ===============================================================

print("\n============== Final Summary ==============")

print("""

Assignment (=)

Two names

One object


copy.copy()

Copies only the outer object.

Nested mutable objects
are SHARED.


copy.deepcopy()

Copies everything.

Outer object

Nested lists

Nested dictionaries

Nested sets

Everything becomes independent.


Golden Rule

If you MODIFY a shared nested object

append()

remove()

pop()

extend()

sort()

Both original and shallow copy change.


If you REPLACE the reference

copied[0] = [100]

copied[0] = 100

Only the copied list changes.


Deep Copy

Nothing is shared.

Changes NEVER affect the original.

""")