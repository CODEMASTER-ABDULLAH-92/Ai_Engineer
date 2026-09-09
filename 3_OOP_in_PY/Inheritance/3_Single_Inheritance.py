# ==============================
# Single Inheritance
# ==============================

# Single inheritance means that one child class inherits from one parent class.


class Animal:          # Parent class

    def eat(self):
        print("Animal is eating")


class Dog(Animal):     # Child class

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# | Type             | Structure                        |
# | ---------------- | -------------------------------- |
# | Single       | One parent → One child           |
# | Multiple     | Multiple parents → One child     |
# | Multilevel   | Parent → Child → Grandchild      |
# | Hierarchical | One parent → Multiple children   |
# | Hybrid       | Combination of inheritance types |
