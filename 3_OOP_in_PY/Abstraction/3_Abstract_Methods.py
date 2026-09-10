# ============================================================
# ABSTRACT METHODS IN PYTHON
# ============================================================

# What is an Abstract Method?
#
# An abstract method is a method that is declared in an
# abstract class but is not implemented there.
#
# It tells child classes that they MUST provide
# their own implementation of this method.
#
#
# ------------------------------------------------------------
# CREATING AN ABSTRACT METHOD
# ------------------------------------------------------------
#
# We use the `@abstractmethod` decorator from the `abc` module.
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
# `make_sound()` is an abstract method.
#
# `@abstractmethod`:
# Marks the method as abstract.
#
# `pass`:
# Means there is no implementation in the parent
# in this example.
#
#
# ------------------------------------------------------------
# PURPOSE OF AN ABSTRACT METHOD
# ------------------------------------------------------------
#
# The abstract method defines WHAT the child class
# must implement.
#
# Example:
#
# Animal → must have make_sound()
#
# The Animal class does not decide exactly how every
# animal will make a sound.
#
#
# ------------------------------------------------------------
# CHILD CLASS IMPLEMENTATION
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
# ANOTHER CHILD CLASS
# ------------------------------------------------------------
#
# class Cat(Animal):
#
#     def make_sound(self):
#         print("Meow")
#
#
# cat = Cat()
# cat.make_sound()
#
# Output:
#
# Meow
#
#
# ------------------------------------------------------------
# WHAT IF THE CHILD DOES NOT IMPLEMENT THE METHOD?
# ------------------------------------------------------------
#
# class Dog(Animal):
#     pass
#
#
# dog = Dog()
#
# This causes an error because Dog has not implemented
# the required abstract method make_sound().
#
#
# ------------------------------------------------------------
# IMPORTANT RULE
# ------------------------------------------------------------
#
# A concrete child class must implement ALL abstract methods
# inherited from the parent before its objects can be created.
#
#
# ------------------------------------------------------------
# ABSTRACT METHOD VS NORMAL METHOD
# ------------------------------------------------------------
#
# Normal method:
#
# def eat(self):
#     print("Eating")
#
# The parent provides the implementation.
#
#
# Abstract method:
#
# @abstractmethod
# def make_sound(self):
#     pass
#
# The child class is required to provide the implementation.