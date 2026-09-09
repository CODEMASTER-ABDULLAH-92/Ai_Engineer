# Hybrid Inheritance in Python OOP

# Hybrid inheritance is a combination of two or more types of inheritance in a single program.

# For example, you can combine hierarchical inheritance + multiple inheritance.

class Animal:
    
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    
    def meow(self):
        print("Cat is meowing")


class Hybrid(Dog, Cat):
    
    def play(self):
        print("Hybrid is playing")

obj = Hybrid()
obj.eat()
obj.bark()
obj.meow()
obj.play()


# | Inheritance      | Structure                        |
# | ---------------- | -------------------------------- |
# | Single       | A → B                            |
# | Multiple     | A + B → C                        |
# | Multilevel   | A → B → C                        |
# | Hierarchical | A → B and A → C                  |
# | Hybrid       | Combination of two or more types |
