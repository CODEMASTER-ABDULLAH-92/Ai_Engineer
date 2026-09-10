from abc import ABC, abstractmethod


class Animal(ABC):              # Abstract class

    @abstractmethod
    def make_sound(self):       # Abstract method
        pass                    # No implementation here


class Dog(Animal):              # Child class

    def make_sound(self):       # Implementation
        print("Bark")


class Cat(Animal):              # Child class

    def make_sound(self):       # Implementation
        print("Meow")

dog = Dog()
cat = Cat()
cat.make_sound()
dog.make_sound()