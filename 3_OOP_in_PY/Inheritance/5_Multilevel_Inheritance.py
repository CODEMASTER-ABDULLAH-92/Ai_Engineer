# Multilevel Inheritance in Python OOP

# Multilevel inheritance means inheritance happens in multiple levels, where a child class becomes the parent of another class.


class Grandfather:

    def house(self):
        print("Grandfather has a house")


class Father(Grandfather):

    def car(self):
        print("Father has a car")


class Son(Father):

    def bike(self):
        print("Son has a bike")

son = Son()

son.house()
son.car()
son.bike()
