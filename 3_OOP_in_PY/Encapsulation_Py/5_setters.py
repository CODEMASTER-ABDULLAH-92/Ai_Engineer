# Setters in Python

# A setter is a method used to set, change, or update the value of an attribute, especially a private attribute.

# Setters are commonly used with encapsulation because they allow us to control how private data is modified.
class Student:
    def __init__(self):
        self.__age = 20

    def set_age(self, age):
        self.__age = age
    
# __age → private attribute
# set_age() → setter
# age → new value
# self.__age = age → changes the private attribute



# getter --> reads the value 
# setter --> change the value 




class Student:
    def __init__(self):
        self.__age = 20

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age >= 0:
            self.__age = age

student = Student()

print(student.get_age())  # Read

student.set_age(25)       # Change

print(student.get_age())  # Read updated value