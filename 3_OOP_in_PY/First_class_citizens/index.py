# =============================================
# # First-Class Citizens in Python
# =============================================

# First-class citizen means that something in Python is treated like a normal value/object.
# In Python, functions are first-class citizens.
# That means you can treat a function like you treat an `int`, `str`, or any other object.



# A function can be:

# =============================================
# 1. Stored in a variable
# =============================================

def hello():
    print("Hello")

x = hello
x()


# =============================================
# 2. Passed as an argument
# =============================================


def hello():
    print("Hello")

def execute(func):
    func()

execute(hello)




# =============================================
# 3. Returned from another function
# =============================================


def outer():
    def inner():
        print("Hello")

    return inner

my_function = outer()
my_function()


# =============================================
# 4. Stored inside a data structure
# =============================================


def add():
    print("Add")

def subtract():
    print("Subtract")

functions = [add, subtract]

functions[0]()
functions[1]()
