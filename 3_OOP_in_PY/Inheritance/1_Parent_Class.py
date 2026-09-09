# ======================================
# Parent Class in Python OOP
# ====================================== 

# --> A parent class is a class that provides attributes and methods to another class. The class that receives them is called the child class.

# --> It is also called a base class or superclass.

class Animal:
    
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()    # inherited from Animal
dog.bark()  # belongs to Dog

# Animal is eating
# Dog is barking
