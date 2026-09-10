# ============================================================
# ABSTRACT CLASS IN PYTHON
# ============================================================

# What is an Abstract Class?
#
# An abstract class is a class that is designed to be
# a blueprint for other classes.
#
# It defines what functionality child classes must provide,
# but can leave the actual implementation to the child classes.
#--> That has at least one abstract method. 
#
# ------------------------------------------------------------
# CREATING AN ABSTRACT CLASS
# ------------------------------------------------------------
#
# We use ABC from Python's built-in `abc` module.
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
# Animal is an Abstract Class.
#
# `ABC`:
# Makes the class an Abstract Base Class.
#
# `@abstractmethod`:
# Makes the method an Abstract Method.
#
#
# ------------------------------------------------------------
# ABSTRACT METHOD
# ------------------------------------------------------------
#
# An abstract method defines what the child class MUST provide.
#
# Example:
#
# @abstractmethod
# def make_sound(self):
#     pass
#
#
# The parent class does not provide the actual implementation
# in this beginner example.
#
# The child class provides the implementation.
#
#
# ------------------------------------------------------------
# CHILD CLASS
# ------------------------------------------------------------
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
#
#
# ------------------------------------------------------------
# CAN WE CREATE AN OBJECT OF AN ABSTRACT CLASS?
# ------------------------------------------------------------
#
# No.
#
# Example:
#
# animal = Animal()
#
# This gives an error because Animal still has an
# unimplemented abstract method.
#
#
# But we can create an object of Dog:
#
# dog = Dog()
#
# because Dog has implemented make_sound().
#
#
# ------------------------------------------------------------
# ABSTRACT CLASS AS A BLUEPRINT
# ------------------------------------------------------------
#
#             Animal
#          (Abstract Class)
#                 |
#          make_sound()
#                 |
#          ----------------
#          |              |
#         Dog            Cat
#          |              |
#        Bark            Meow
#
#
# Animal defines WHAT must exist.
#
# Dog and Cat define HOW it works.