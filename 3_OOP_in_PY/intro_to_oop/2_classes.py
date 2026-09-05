# What is a Class in Python OOP?

# A class is a blueprint or template used to create objects.

# It defines:

# What data (attributes) an object will have.
# What actions (methods) an object can perform.

# A class itself is not an object. It is the design from which objects are created.


class Car:
    pass


# ===================================
# A Class with Attributes
# ===================================

# Suppose every car has a brand and a color.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color



# What Does self Mean?

# Inside a class, self refers to the current object.



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduction(self):
        print(f"My name is {self.name}. And i am {self.age} years old.")
    

s1 = Student("Muhammad Abdullah", 23)
s2 = Student("Rajab Ali", 20)

s1.introduction()
s2.introduction()


#.                    CLASS
#.               +----------------+
#.               |    Student     |
#.               |----------------|
#.               | name           |
#.               | age            |
#.               | introduce()    |
#.               +----------------+
#.                      |
#.             Creates Objects
#.               /            \
#.              /              \
#.     +----------------+   +----------------+
#.     |   student1     |   |   student2     |
#.     |----------------|   |----------------|
#.     | name = Ali     |   | name = Sara    |
#.     | age = 20       |   | age = 22       |
#.     +----------------+   +----------------+
