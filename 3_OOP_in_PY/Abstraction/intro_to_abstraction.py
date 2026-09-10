# ============================================================
# ABSTRACTION IN PYTHON OOP
# ============================================================

# What is Abstraction?
#
# Abstraction in OOP means:
# Hiding unnecessary implementation details
# and showing only the essential features to the user.
#
# In simple words:
#
# Abstraction = Hide the "HOW" and show the "WHAT".
#
#
# ------------------------------------------------------------
# REAL-LIFE EXAMPLE
# ------------------------------------------------------------
#
# Think about driving a car.
#
# You use:
#
# Steering wheel  → to turn
# Brake           → to stop
# Accelerator     → to increase speed
#
# You don't need to know exactly how the engine,
# fuel injection, transmission, sensors, etc. work internally.
#
# You only use the essential controls.
#
# This is called ABSTRACTION.
#
#
# ------------------------------------------------------------
# PROGRAMMING EXAMPLE
# ------------------------------------------------------------
#
# Suppose we have a Car class:
#
# class Car:
#
#     def start(self):
#         print("Car started")
#
#
# You can simply do:
#
# car = Car()
# car.start()
#
# You don't need to know what happens internally
# inside the start() method.
#
# The user only knows:
#
# start() → starts the car
#
# The user does NOT need to know about:
#
# fuel system
# engine ignition
# battery
# sensors
# etc.
#
# This is abstraction.
#
#
# ------------------------------------------------------------
# ABSTRACTION IN PYTHON
# ------------------------------------------------------------
#
# Python provides the `abc` module for implementing
# formal abstraction.
#
# Example:
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# Here, Animal is an abstract class.
#
# It says:
#
# Every animal MUST have a make_sound() method,
# but Animal does not specify exactly how it should work.
#
#
# ------------------------------------------------------------
# CHILD CLASS IMPLEMENTATION
# ------------------------------------------------------------
#
# The child class provides the actual implementation:
#
# class Dog(Animal):
#
#     def make_sound(self):
#         print("Bark")
#
#
# dog = Dog()
# dog.make_sound()
#
# Output:
#
# Bark