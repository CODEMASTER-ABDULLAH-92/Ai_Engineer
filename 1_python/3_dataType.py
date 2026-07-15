"""
Python Data Types
-----------------
A data type defines the kind of value a variable can store.
Python automatically detects the data type when you assign a value.
"""

"""
Common Python Data Types:
1. int       -> Whole numbers
2. float     -> Decimal numbers
3. str       -> Text data
4. bool      -> True or False
5. list      -> Ordered, changeable collection
6. tuple     -> Ordered, unchangeable collection
7. dict      -> Key-value pairs
8. set       -> Unordered unique values
9. NoneType  -> Represents no value
"""


num = (1,2,3,4,5)
# last = num.pop()
# print(last)
print(num[1])
# Integer (int)
from typing import Literal


age = 20
print("Integer:", age)
print(type(age))

# Float (float)
price = 99.99
print("\nFloat:", price)
print(type(price))

# String (str)
name = "Abdullah"
print("\nString:", name)
print(type(name))

# Boolean (bool)
is_student = True
print("\nBoolean:", is_student)
print(type(is_student))

# List (list)
fruits = ["apple", "banana", "mango"]
print("\nList:", fruits)
print(type[str](fruits))

# Tuple (tuple)
coordinates = (10, 20)
print("\nTuple:", coordinates)
print(type[Literal[10, 20], ...](coordinates))

# Dictionary (dict)
student = {
    "name": "Abdullah",
    "age": 20,
    "course": "Software Engineering"
}
print("\nDictionary:", student)
print(type(student))

# Set (set)
numbers = {1, 2, 3, 4}
print("\nSet:", numbers)
print(type(numbers))

# None Type (NoneType)
value = None
print("\nNone Type:", value)
print(type(value))

