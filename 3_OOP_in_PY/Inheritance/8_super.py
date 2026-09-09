# ================================
# super() in Python OOP
# ================================

# super() is used in a child class to access methods or attributes of its parent class.

# Most commonly, we use super() to call the parent class's __init__() method or another parent method.

class Parent:
    def __init__(self):
        print("Parent Constructor")
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

obj = Child()

# super().__init__() says: ==> Call the __init__() method of my parent class.


# 2. Why do we need super()?

# Suppose the parent has some important initialization:

class Person:
    def __init__(self, name):
        self.name = name

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child = Child("Muhammad Abdullah: ", 23)
print(child.name)
print(child.age)

