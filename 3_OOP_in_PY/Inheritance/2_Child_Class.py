# =====================================
# Child Class in Python OOP
# =====================================

# A child class is a class that inherits attributes and methods from a parent class.

# It is also called a subclass or derived class.

class Animal:          # Parent class
    
    def eat(self):
        print("Animal is eating")


class Dog(Animal):     # Child class
    
    def bark(self):
        print("Dog is barking")

# Dog is the child class because it inherits from Animal.