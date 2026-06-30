# ====================
# Function?
# ====================

# A function is a reusable block of code that performs a specific task. It helps you:
# Avoid code duplication (DRY - Don't Repeat Yourself)
# Organize code into logical pieces
# Make code more readable and maintainable


def greet():
    print("Hello")

# greet()


# ================================================
# Function with Arguments (Parameters)
# ================================================

def greet(name): #name is the parameter
    print(f"Hello {name}")

# Calling the function with the arguments
# greet("Muhammad Abdullah")
# greet("Rajab Ali")



# =====================================
# Positional Arguments (Order matters)
# =====================================

def greet(name, age):
    print(f"name: {name}\nage: {age}")

# greet("Muhammad Abdullah", 23) #Correct
# greet(22, "Rajab Ali") #Wrong, Values in the wrong order.



# =====================================
# Keyword Arguments (Order doesn't matter)
# =====================================

def greet(name, age):

    print(f"Name: {name}\nAge: {age}")

# greet(age=23, name="Muhammad Abdullah")


# =====================================
# Default Arguments (Optional parameters)
# =====================================

def greet(name, greeting="Hello"):  # greeting has default value
    print(f"{greeting}, {name}!")

# greet("Alice")           # Output: Hello, Alice!
# greet("Bob", "Hi")       # Output: Hi, Bob!
# greet("Charlie", "Hey")  # Output: Hey, Charlie!



# =====================================
# Variable-Length Arguments
# =====================================


# *args - Non-keyword arguments (Tuple)

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1,2,3,4,5))



# **kwargs - Keyword arguments (Dictionary)


def handle_dict(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} :{val}")

# handle_dict(name="Muhammad Abdullah", age=23, roll_number="234245")


# ================================

# Write a function called greet_user() that takes a name as an argument and prints "Hello, [name]!". Call the function with your name.

# ================================

def greet_user(name="Rajab"):

    print(f"Hello, {name}")


# greet_user("Muhammad Abdullah")




# ================================

# Write a function called square_number() that takes a number as input and returns its square. Test it with the number 7.

# ================================


def square_number():
    val = int(input("Enter the number: "))

    return val*val

val = square_number()
# print(val)
