# ============================================================
# PICKLE IN PYTHON
# Serialization and Deserialization
# ============================================================

# Pickle is a built-in Python module.
#
# It is used to:
# 1. Serialize Python objects
# 2. Save them into a binary file
# 3. Deserialize them later
# 4. Reconstruct the Python objects again
#
# Simple meaning:
#
#     Python Object
#          ↓
#       Pickle
#          ↓
#     Binary Data
#          ↓
#        File
#
# And later:
#
#        File
#          ↓
#       Pickle
#          ↓
#     Python Object


import pickle


# ============================================================
# 1. WHY DO WE NEED PICKLE?
# ============================================================

# Python objects normally live in RAM (memory).
#
# When the program ends, those objects normally disappear.
#
# Example:
#
#     person = Person("Abdullah", 23)
#
# The object exists while the program is running.
#
# If we want to save that object and use it later,
# we can use Pickle.
#
# Pickle allows us to store Python objects in a file.


# ============================================================
# 2. CUSTOM CLASS
# ============================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Muhammad Abdullah", 23)

print(person.name)
print(person.age)


# ============================================================
# 3. SERIALIZATION
# ============================================================

# Serialization means:
#
#     Python Object → Serialized Data
#
# With Pickle, the object is converted into a
# Python-specific binary representation.
#
# pickle.dump() is used to serialize an object
# and write it directly into a file.


with open("person.pkl", "wb") as f:
    pickle.dump(person, f)


# Now the Person object has been serialized
# and stored inside:
#
#     person.pkl
#
# The file contains binary data.
# It is not designed to be human-readable.


# ============================================================
# 4. DESERIALIZATION
# ============================================================

# Deserialization means:
#
#     Serialized Data → Python Object
#
# pickle.load() reads the binary data
# and reconstructs the Python object.


with open("person.pkl", "rb") as f:
    person = pickle.load(f)


print(person.name)
print(person.age)

# Output:
# Muhammad Abdullah
# 23


# ============================================================
# 5. CHECK THE OBJECT TYPE
# ============================================================

# One powerful feature of Pickle is that it can
# reconstruct the Python object.
#
# So after loading:

print(type(person))

# Output will normally look like:
#
# <class '__main__.Person'>
#
# This means we got a Person object back.


# ============================================================
# 6. JSON vs PICKLE
# ============================================================

# JSON and Pickle both provide serialization
# and deserialization.
#
# But they work differently.


# -------------------------
# JSON
# -------------------------

# JSON mainly works with standard data types:
#
#     string
#     number
#     list
#     dictionary
#     boolean
#     null
#
# A custom Python object usually needs to be
# converted into JSON-compatible data first.
#
#
# Example:
#
#     Person Object
#          ↓
#      Dictionary
#          ↓
#         JSON
#
#
# JSON example:
#
# {
#     "name": "Muhammad Abdullah",
#     "age": 23
# }
#
#
# JSON is:
#
# - Human-readable
# - Language-independent
# - Commonly used with APIs
# - Good for communication between different languages


# -------------------------
# PICKLE
# -------------------------

# Pickle is Python-specific.
#
# It can serialize many Python objects directly.
#
#
# Example:
#
#     Person Object
#          ↓
#       Pickle
#          ↓
#     Binary Data
#
#
# We don't normally need to manually convert:
#
#     Person → Dictionary
#
# before using Pickle.


# ============================================================
# 7. MAIN DIFFERENCE
# ============================================================

# JSON:
#
#     Python Object
#          ↓
#     JSON-compatible data
#          ↓
#     JSON text
#
#
# Pickle:
#
#     Python Object
#          ↓
#     Pickle serialization
#          ↓
#     Binary data


# ============================================================
# 8. PICKLE CAN SAVE MANY PYTHON OBJECTS
# ============================================================

# Pickle can serialize many built-in Python objects,
# such as:
#
# - list
# - tuple
# - dictionary
# - set
# - custom class instances
# - and many other Python objects
#
# Example:

data = {
    "name": "Abdullah",
    "age": 23,
    "skills": ["Python", "JavaScript", "React"]
}


with open("data.pkl", "wb") as f:
    pickle.dump(data, f)


with open("data.pkl", "rb") as f:
    data = pickle.load(f)


print(data)


# ============================================================
# 9. TRANSFERRING A PICKLE FILE
# ============================================================

# A Pickle file can be:
#
# - saved
# - copied
# - moved
# - backed up
# - transferred to another location
#
#
# Example:
#
# Project A:
#
#     project_a/
#         person.pkl
#
#
# We can copy the file to:
#
# Project B:
#
#     project_b/
#         person.pkl
#
#
# Then another Python program can load it:
#
#     with open("person.pkl", "rb") as f:
#         person = pickle.load(f)
#
#
# The important point:
#
# Pickle is mainly designed for Python-to-Python
# object serialization.


# ============================================================
# 10. USING ANOTHER FILE PATH
# ============================================================

# The Pickle file doesn't have to be in the
# current directory.
#
# We can specify a path.


# Example:
#
# with open("data/person.pkl", "rb") as f:
#     person = pickle.load(f)
#
#
# Or:
#
# with open("backup/person.pkl", "rb") as f:
#     person = pickle.load(f)
#
#
# The path tells Python where the Pickle file is located.


# ============================================================
# 11. REAL-WORLD USE CASES
# ============================================================

# Pickle can be useful when you want to save
# Python-specific data and load it later.
#
#
# USE CASE 1: Save trained machine-learning models
# ------------------------------------------------
#
# A machine-learning model may contain a complex
# Python object with many learned values.
#
# We can serialize the model and save it.
#
# Later, we can load the model instead of training it again.
#
#
# Concept:
#
#     Trained Model
#          ↓
#       Pickle
#          ↓
#     model.pkl
#
# Later:
#
#     model.pkl
#          ↓
#       Pickle
#          ↓
#     Trained Model


# ============================================================
# USE CASE 2: Save Python application state
# ============================================================

# Suppose an application has:
#
#     users
#     settings
#     objects
#     configuration
#     application state
#
# Pickle can be used to save Python-specific
# application data for later use.


# ============================================================
# USE CASE 3: Caching
# ============================================================

# Suppose your program performs an expensive calculation.
#
# Instead of calculating the same thing again,
# you can save the result using Pickle.
#
#
# First time:
#
#     Expensive calculation
#            ↓
#        Pickle file
#
#
# Next time:
#
#     Pickle file
#            ↓
#      Load saved result
#
# This can save processing time.


# ============================================================
# USE CASE 4: Save complex Python data
# ============================================================

# If your application has complex Python data structures,
# Pickle can be convenient because you don't have to
# manually convert every object into a dictionary.


# ============================================================
# 12. IMPORTANT: PICKLE IS PYTHON-SPECIFIC
# ============================================================

# Pickle is designed mainly for Python.
#
# For example:
#
#     Python → Pickle → Python
#
# works naturally.
#
#
# But:
#
#     Python → Pickle → JavaScript
#
# is not the normal use case.
#
#
# If you need communication between:
#
#     Python
#     JavaScript
#     Java
#     C#
#     PHP
#
# JSON or another language-independent format
# is usually more appropriate.


# ============================================================
# 13. IMPORTANT SECURITY WARNING
# ============================================================

# NEVER load a Pickle file from an untrusted source.
#
# For example:
#
#     pickle.load(f)
#
# can execute malicious code if the Pickle file
# has been specially crafted.
#
# Therefore:
#
#     Only unpickle files that you trust.
#
#
# Safe idea:
#
#     Your own pickle file
#            ↓
#        pickle.load()
#
#
# Dangerous idea:
#
#     Unknown internet file
#            ↓
#        pickle.load()
#
# Avoid this.


# ============================================================
# 14. dump() vs load()
# ============================================================

# pickle.dump()
#
#     Python Object
#          ↓
#     Binary file
#
#
# pickle.load()
#
#     Binary file
#          ↓
#     Python Object
#
#
# Easy way to remember:
#
#     dump = put/save
#     load = get/read


# ============================================================
# 15. dumps() vs dump()
# ============================================================

# There are also:
#
#     pickle.dumps()
#     pickle.loads()
#
#
# Difference:
#
# dump():
#     Object → file
#
#
# dumps():
#     Object → bytes
#
#
# load():
#     file → object
#
#
# loads():
#     bytes → object


# Example:

person = Person("Abdullah", 23)

# Object → bytes
serialized_person = pickle.dumps(person)

print(type(serialized_person))

# Output:
#
# <class 'bytes'>


# Bytes → object
person = pickle.loads(serialized_person)

print(person.name)
print(person.age)


# ============================================================
# 16. COMPLETE PICKLE FLOW
# ============================================================

# SERIALIZATION:
#
#     Python Object
#           ↓
#     pickle.dump()
#           ↓
#     Binary File
#
#
# DESERIALIZATION:
#
#     Binary File
#           ↓
#     pickle.load()
#           ↓
#     Python Object
#
#
# ------------------------------------------------------------
#
# If using bytes directly:
#
#     Python Object
#           ↓
#     pickle.dumps()
#           ↓
#     bytes
#
#
#     bytes
#           ↓
#     pickle.loads()
#           ↓
#     Python Object


# ============================================================
# 17. FINAL SUMMARY
# ============================================================

# Pickle:
#
#     - Python's serialization module
#     - Converts Python objects into serialized binary data
#     - Can save many Python objects directly
#     - Can reconstruct those objects later
#     - Uses binary files
#     - Mainly used for Python-to-Python data
#     - Useful for persistence, caching, ML models, etc.
#     - Should NEVER be used with untrusted Pickle files
#
#
# The most important functions:
#
#     pickle.dump()   → object → file
#     pickle.load()   → file → object
#
#     pickle.dumps()  → object → bytes
#     pickle.loads()  → bytes → object
#
#
# ============================================================
# MEMORY TRICK
# ============================================================
#
#     PICKLE = PACK AND UNPACK PYTHON OBJECTS
#
#     dump  → SAVE
#     load  → RESTORE
#
#     dumps → object to bytes
#     loads → bytes to object
#
# ============================================================