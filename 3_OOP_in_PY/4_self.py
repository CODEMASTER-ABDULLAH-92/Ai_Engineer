# ============================================================
# SELF IN PYTHON
# ============================================================
#
# `self` refers to the CURRENT OBJECT (instance).
#
# It is used inside a class to access:
# 1. Attributes of the current object
# 2. Methods of the current object
#
# Easy way to remember:
#
# self = current object


# ============================================================
# BASIC EXAMPLE
# ============================================================

class Student:

    def __init__(self, name, age):
        # self.name = attribute of the current object
        # name     = value received as a parameter

        self.name = name
        self.age = age

    def introduce(self):
        print("My name is:", self.name)
        print("My age is:", self.age)


# Create an object
student1 = Student("Ali", 20)

# Call the method
student1.introduce()




# ============================================================
# self.name vs name
# ============================================================

class Student:

    def __init__(self, name):
        # name:
        # Local parameter

        # self.name:
        # Attribute stored inside the object

        self.name = name


student1 = Student("Ali")

print(student1.name)


# ============================================================
# MORE THAN ONE ATTRIBUTE
# ============================================================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.show_info()
car2.show_info()


# ============================================================
# self WITH MULTIPLE METHODS
# ============================================================

class Calculator:

    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def cube(self):
        return self.number * self.number * self.number


calculator = Calculator(5)

print("Square:", calculator.square())
print("Cube:", calculator.cube())


# ============================================================
# IMPORTANT CONCEPT
# ============================================================
#
# When we write:
#
# student1.introduce()
#
# Python conceptually passes student1 as `self`.
#
# It is similar to:
#
# Student.introduce(student1)
#
# Therefore:
#
# self → student1
#
# Similarly:
#
# student2.introduce()
#
# self → student2


# ============================================================
# WHY DO WE NEED self?
# ============================================================
#
# Because every object can have different data.
#
# Example:
#
# student1.name = "Ali"
# student2.name = "Ahmed"
#
# The same method can work with different objects because
# `self` tells Python which object we are working with.


# ============================================================
# EASY RULE TO REMEMBER
# ============================================================
#
# self = current object
#
# self.name
#     ↓
# name belonging to the current object
#
# self.age
#     ↓
# age belonging to the current object
#
# self.method()
#     ↓
# method belonging to the current object


# ============================================================
# IMPORTANT NOTE
# ============================================================
#
# `self` is not a special Python keyword.
#
# It is the standard and recommended name for the first
# parameter of an instance method.
#
# Always use `self` because it is the Python convention.