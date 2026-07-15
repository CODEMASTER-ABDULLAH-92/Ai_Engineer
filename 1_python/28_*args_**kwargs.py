"""
===============================================================
              *ARGS and **KWARGS IN PYTHON
        (Complete Beginner Friendly Guide)
===============================================================

Imagine you are giving gifts to your friend.

Your friend says:

"Bring me some gifts."

But...

He never tells you HOW MANY gifts.

Maybe

🎁

Maybe

🎁 🎁 🎁

Maybe

🎁 🎁 🎁 🎁 🎁 🎁

The number is unknown.

Python solves this problem using

*args

---------------------------------------------------------------

Now imagine your friend says

"Bring gifts, but also tell me their details."

Example

Toy = Car

Color = Red

Price = 500

Now every value has a NAME.

Python solves this using

**kwargs

"""


# ===============================================================
# Without *args
# ===============================================================

print("============== Without *args ==============")


def add(a, b):
    print(a + b)


add(10, 20)

"""
Works

But

add(10,20,30)

will give an error.

Because the function
expects ONLY TWO arguments.
"""


# ===============================================================
# *args Example
# ===============================================================

print("\n============== *args Example ==============")


def show_numbers(*args):
    print(args)


show_numbers(10)

show_numbers(10, 20)

show_numbers(10, 20, 30)

show_numbers(10, 20, 30, 40)

"""
Output

(10,)

(10,20)

(10,20,30)

(10,20,30,40)

Notice

args is stored
as a TUPLE.
"""


# ===============================================================
# Different Name
# ===============================================================

print("\n============== Different Names ==============")


def numbers(*items):
    print(items)


numbers(1, 2, 3)

"""
The name

args

is NOT special.

These are all valid.

*numbers

*items

*values

*anything

The IMPORTANT part is

*
"""


# ===============================================================
# Sum Example
# ===============================================================

print("\n============== Total Bill ==============")


def total_bill(*prices):
    print(sum(prices))


total_bill(100)

total_bill(100, 200)

total_bill(100, 200, 300)

"""
Output

100

300

600

Perfect for
Shopping carts
Invoices
Bills
where the number
of items is unknown.
"""


# ===============================================================
# Loop Through *args
# ===============================================================

print("\n============== Loop Through *args ==============")


def display(*numbers):
    for number in numbers:
        print(number)


display(10, 20, 30)

"""
Output

10

20

30
"""


# ===============================================================
# What is **kwargs
# ===============================================================

print("\n============== **kwargs Example ==============")


def person(**kwargs):
    print(kwargs)


person(name="Ali", age=20)

"""
Output

{'name':'Ali','age':20}

kwargs is stored
as a DICTIONARY.
"""


# ===============================================================
# Access Values
# ===============================================================

print("\n============== Access Dictionary Values ==============")


def student(**details):
    print(details["name"])
    print(details["age"])


student(name="Ali", age=20)

"""
Output

Ali

20
"""


# ===============================================================
# Loop Through kwargs
# ===============================================================

print("\n============== Loop Through **kwargs ==============")


def information(**details):
    for key, value in details.items():
        print(key, "=", value)


information(name="Ali", age=20, city="Lahore")

"""
Output

name = Ali

age = 20

city = Lahore
"""


# ===============================================================
# *args vs **kwargs
# ===============================================================

print("\n============== *args ==============")


def example(*args):
    print(args)


example(10, 20, 30)

"""
Output

(10,20,30)

Tuple
"""


print("\n============== **kwargs ==============")


def example2(**kwargs):
    print(kwargs)


example2(a=10, b=20)

"""
Output

{'a':10,'b':20}

Dictionary
"""


# ===============================================================
# Use Both Together
# ===============================================================

print("\n============== *args and **kwargs Together ==============")


def demo(*args, **kwargs):
    print(args)

    print(kwargs)


demo(10, 20, name="Ali", age=20)

"""
Output

(10,20)

{'name':'Ali','age':20}
"""


# ===============================================================
# Real World Example
# ===============================================================

print("\n============== Online Shopping Example ==============")


def order(*products, **customer):
    print("Products :", products)

    print("Customer :", customer)


order(
    "Laptop",
    "Mouse",
    "Keyboard",
    name="Ali",
    city="Faisalabad",
    phone="03001234567"
)

"""
Output

Products

('Laptop','Mouse','Keyboard')

Customer

{
'name':'Ali',
'city':'Faisalabad',
'phone':'03001234567'
}
"""


# ===============================================================
# Argument Order
# ===============================================================

print("\n============== Argument Order ==============")


def student(name, *marks, **details):
    print("Name :", name)

    print("Marks :", marks)

    print("Details :", details)


student(
    "Ali",
    80,
    90,
    85,
    city="Lahore",
    age=20
)

"""
Output

Name

Ali

Marks

(80,90,85)

Details

{'city':'Lahore','age':20}
"""

# ===============================================================
# Comparison Table
# ===============================================================

print("\n============== Comparison ==============")

print("""

*args

Accepts

Positional Arguments

Stored As

Tuple

Example

func(1,2,3)


**kwargs

Accepts

Keyword Arguments

Stored As

Dictionary

Example

func(name="Ali",age=20)

""")

# ===============================================================
# Final Summary
# ===============================================================

print("\n============== Final Summary ==============")

print("""

*args

Accepts any number
of positional arguments.


Stored as
Tuple


**kwargs

Accepts any number
of keyword arguments.


Stored as
Dictionary


Remember: 

The names args and kwargs are only conventions.
""")