# ============================================================
# OBJECT CREATION AND OBJECT REFERENCE
# ============================================================


class Person:

    def __init__(self):
        self.name = "Abdullah"
        self.age = 23


# ------------------------------------------------------------
# 1. OBJECT CREATION
# ------------------------------------------------------------

Person()

# Person() creates a Person object.
#
# The object is created, but we do not store its reference
# in a variable.
#
# Therefore, we cannot directly access that object afterward.


# ------------------------------------------------------------
# 2. OBJECT CREATION WITH A REFERENCE
# ------------------------------------------------------------

P = Person()

# Person() -> creates a Person object
#
# P -> variable that holds a reference to the object
#
# P is NOT the object itself.
#



# ------------------------------------------------------------
# 3. ACCESSING THE OBJECT THROUGH THE REFERENCE
# ------------------------------------------------------------

print(P.name)
print(P.age)
# Output:
# Abdullah
# 23



q  = P # This is valid 
print(q.name)
print(P.name)
# Both are the same 