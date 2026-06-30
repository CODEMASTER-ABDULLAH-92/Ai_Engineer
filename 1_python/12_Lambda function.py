# A lambda function is just a small, quick function that you create in one line.

# Instead of creating

def add(x):
    return x + 1

# You can use 

lambda x : x + 1
# Take x and return x + 1"


# Syntax 

# lambda parameter : expression 

# lambda → tells Python we're creating a lambda function
# x → input
# : → separates input from work
# x * x → result to return

def square(x):
    return x*x
# print(square(2))

square = lambda x : x*x
print(square(2))



# Multiple Inputs
# You can also take two or more inputs 

add = lambda a, b, c : a + b + c
print(add(1,2,3))



largest = lambda a, b : a if a > b else b


# which is equalvilant to 
def largest(a, b):
    if a > b:
        return a
    else:
        return b

# print(largest(10,20))


# ==========================================================
# What is the Map Function in PY 
# ==========================================================

# map() is a built-in Python function that applies a function to every item in an iterable (like a list) and returns a map object.

# ==========================================================
# Syntax:
# ==========================================================



# map(function, iterable)


# 1: function: The function to apply to each item
# 2: iterable: The list/tuple/etc. containing the items

# 

# ==========================================================
# Map With lambda Function 
# ==========================================================

val = tuple(map(lambda x : x * x, [1, 2, 3, 4, 5]))
# print(val)

# Here this is the example of the Map without the lambda function 

def square(x):
    return x * x

val = list(map(square, [1,2,3,4,5]))
# print(val)




# ==========================================================
# Lambda with filter()
# ==========================================================

# filter() keeps only items that satisfy a condition.


# WithOut lambda Function 
def check_is_even(x):
    return x % 2 == 0

val = list(filter(check_is_even, [1,2,3,4]))
# print(val)



# With lambda Function 

val = list(filter(lambda x : x % 2 == 0, [1,2,3,4]))
# print(val)


# ==========================================================
# Positive, Negative, or Zero
# ==========================================================


val = lambda x : "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")

# print(val(0))
# print(val(1))
# print(val(-1))


# Find Maximum of Three Numbers

val = lambda x, y, z : x if y < x > z else (y if x < y > z else z)
print(val(10,20,30))


# Calculate Area of Rectangle

val = lambda length, width : length * width
print(val(4, 5))
