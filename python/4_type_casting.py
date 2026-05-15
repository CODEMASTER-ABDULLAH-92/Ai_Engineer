"""
Python Type Casting
-------------------
Type casting means converting one data type into another.
Python provides built-in functions for type conversion.
For example:

-> Convert string → integer
-> Convert integer → float
-> Convert list → tuple

"""
# String to Integer
num = "10"
converted_num = int(num)

print("String to Integer:")
print(converted_num)
print(type(converted_num))


# Integer to Float
number = 5
float_number = float(number)

print("\nInteger to Float:")
print(float_number)
print(type(float_number))


# Float to Integer
price = 9.99
integer_price = int(price)

print("\nFloat to Integer:")
print(integer_price)
print(type(integer_price))


# Integer to String
age = 20
string_age = str(age)

print("\nInteger to String:")
print(string_age)
print(type(string_age))


# Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

print("\nTuple to List:")
print(my_list)
print(type(my_list))


# List to Tuple
fruits = ["apple", "banana", "mango"]
fruit_tuple = tuple(fruits)

print("\nList to Tuple:")
print(fruit_tuple)
print(type(fruit_tuple))


# List to Set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)

print("\nList to Set:")
print(unique_numbers)
print(type(unique_numbers))


# Integer to Boolean
value = 1
boolean_value = bool(value)

print("\nInteger to Boolean:")
print(boolean_value)
print(type(boolean_value))


"""
Common Type Casting Functions:

1. int()    -> Convert to integer
2. float()  -> Convert to float
3. str()    -> Convert to string
4. list()   -> Convert to list
5. tuple()  -> Convert to tuple
6. set()    -> Convert to set
7. bool()   -> Convert to boolean
"""
