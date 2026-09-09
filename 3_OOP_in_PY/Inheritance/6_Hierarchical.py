# Hierarchical Inheritance in Python OOP

# Hierarchical inheritance means multiple child classes inherit from the same parent class.

    #       Parent
    #      /      \
    #     ↓        ↓
    #  Child 1   Child 2
    

class Animal:          # Parent class

    def eat(self):
        print("Animal is eating")


class Dog(Animal):     # Child class 1

    def bark(self):
        print("Dog is barking")


class Cat(Animal):     # Child class 2

    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
