"""
Constructors in Python (OOP)

A constructor is a special method in a class that is automatically called
when an object is created. In Python, the constructor is __init__().
"""

# --------------------------------------------------------------------
# Example 1: Without Constructor
# --------------------------------------------------------------------

class StudentWithoutConstructor:
    pass

student = StudentWithoutConstructor()
student.name = "Ali"
student.age = 20

print("Without Constructor")
print(student.name)
print(student.age)

# --------------------------------------------------------------------
# Example 2: With Constructor
# --------------------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Ali", 20)

print("\nWith Constructor")
print(student.name)
print(student.age)

# --------------------------------------------------------------------
# Understanding self
# --------------------------------------------------------------------

student1 = Student("Ali", 20)
print("\nUnderstanding self")
print(student1.name)

# --------------------------------------------------------------------
# Multiple Objects
# --------------------------------------------------------------------

student2 = Student("Sara", 22)

print("\nMultiple Objects")
print(student1.name)
print(student2.name)

# --------------------------------------------------------------------
# Constructor with Default Values
# --------------------------------------------------------------------

class StudentDefault:
    def __init__(self, name="Unknown", age=18):
        self.name = name
        self.age = age

student3 = StudentDefault()

print("\nDefault Values")
print(student3.name)
print(student3.age)

# --------------------------------------------------------------------
# Constructor Performing Another Task
# --------------------------------------------------------------------

class Car:
    def __init__(self, brand):
        self.brand = brand
        print("\nCar object created!")

car = Car("Toyota")

# --------------------------------------------------------------------
# Constructor vs Normal Method
# --------------------------------------------------------------------

class StudentGreeting:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

student4 = StudentGreeting("Ali")

print("\nConstructor vs Normal Method")
student4.greet()

# --------------------------------------------------------------------
# Summary
# --------------------------------------------------------------------

print("""
Summary:
- __init__() is the constructor in Python.
- It is called automatically when an object is created.
- It initializes object attributes.
- self refers to the current object.
- Each object has its own instance attributes.
""")