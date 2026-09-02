# ============================================================
# STATIC METHODS
# ============================================================

# Static methods do not use `self` or `cls`.
#

# A static method is a method inside a class that does not depend on the object (self) or the class (cls).


# They are created using @staticmethod.
#
# They don't depend on object or class data.
#
# Example:
#
# class Calculator:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# Calculator.add(10, 20)
#
#
# Easy memory:
#
# self → Object
# cls  → Class
# static → Neither


# HINT:
# Use a static method when the method only needs the
# arguments passed to it and doesn't need self or cls.



class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def check_is_even(num):
        return num % 2 == 0
        
print(Calculator.add(10,20))
print(Calculator.check_is_even(10))



class Student:
    
    def __init__(self, name):
        self.name = name

s1 = Student("Ahmed")
s2 = s1
print(s1.name)
print(s2.name)