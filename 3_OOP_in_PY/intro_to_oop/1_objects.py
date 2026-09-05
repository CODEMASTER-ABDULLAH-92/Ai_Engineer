# In Object-Oriented Programming (OOP), an object is the real thing that you create from a class
# Think of it like this:

# Class = Blueprint (Design)
# Object = Actual Thing Built from the Blueprint
# Real-Life Example

# Imagine a Car.

# A blueprint for a car describes:

# - It has a color.
# - It has a brand.
# - It has a speed.

# But the blueprint itself is not a real car.

# When you manufacture a car from that blueprint, you get an object.



class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = car("BMW", "Black")
car2 = car("Toyota", "Black")

# Car → Class
# car1 → Object
# car2 → Object

# Both car1 and car2 are separate objects created from the same class.

print(car1.brand)
print(car1.brand)





# Objects Have Behaviors (Methods)

# Objects don't just store data—they can also perform actions.

class car:
    def __init__(self, brand):
        self.brand = brand
    
    def starting(self):
        print(f"{self.brand} is starting")
    

car1 = car("BMW")
car2 = car("Toyota")

car1.starting()
car2.starting()





# Every object has two main parts:

# ================================
# 1. State (Attributes)
# ================================


# These are the data stored in the object.
# car.brand
# car.color
# car.speed

# ================================
# 2. Behavior (Methods)
# ================================


# These are the actions the object can perform.
# car.start()
# car.stop()

