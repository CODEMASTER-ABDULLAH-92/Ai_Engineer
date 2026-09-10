# ============================================================
# Method Overriding in Python
# ============================================================

# Method overriding happens when a child class provides its own version of a method that already exists in the parent class.

# In simple words:
# Parent has a method → Child inherits it → Child changes/redefines that method.


# ------------------------------------------------------------
# Example of Method Overriding
# ------------------------------------------------------------

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    # The child class overrides the parent's sound() method
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()     # Output: Animal makes a sound
dog.sound()       # Output: Dog barks


# ------------------------------------------------------------
# What happened?
# ------------------------------------------------------------

# Animal has a sound() method:

# def sound(self):
#     print("Animal makes a sound")


# Dog inherits from Animal:

# class Dog(Animal):


# But Dog creates its own sound() method:

# def sound(self):
#     print("Dog barks")


# Because Dog has its own version of sound(),
# the parent's sound() method is overridden.


# ------------------------------------------------------------
# Why is it called "Overriding"?
# ------------------------------------------------------------

# The child class overrides the behavior
# that it inherited from the parent class.
#
# Parent:
#     sound() → "Animal makes a sound"
#
# Child:
#     sound() → "Dog barks"
#
# When we call:
#
# dog.sound()
#
# Python uses Dog's version of sound()
# instead of Animal's version.


# ------------------------------------------------------------
# Real-World Example
# ------------------------------------------------------------

class Vehicle:

    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):

    # Override the move() method
    def move(self):
        print("Car is driving")


class Boat(Vehicle):

    # Override the move() method
    def move(self):
        print("Boat is sailing")


car = Car()
boat = Boat()

car.move()       # Output: Car is driving
boat.move()      # Output: Boat is sailing


# ------------------------------------------------------------
# Important Point
# ------------------------------------------------------------

# All classes can have the same method name:
#
# move()
#
# But each child class can provide
# its own implementation of that method.
#
# Car  → move() → Car is driving
# Boat → move() → Boat is sailing
#
# This is method overriding.




# ============================================================
# Pattern to Remember
# ============================================================

class Parent:

    def method(self):
        print("Parent")


class Child(Parent):

    def method(self):
        print("Child")


# ============================================================
# Definition to Remember
# ============================================================

# Same method name
#       +
# Parent-child relationship
#       +
# Child provides a new implementation
#       =
# Method Overriding
# ============================================================