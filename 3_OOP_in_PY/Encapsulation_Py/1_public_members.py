# In OOP (Object-Oriented Programming), a public member is a variable (attribute) or function (method) that can be accessed directly from outside the class.

# In simple words:

# Public = accessible from anywhere, including outside the class.

class Student:
    def __init__(self):
        self.name = "Abdullah"   # Public attribute

    def display(self):           # Public method
        print(self.name)

# at here student is not the object, it holds the address the of the object .
student = Student()

print(student.name)      # ✅ Allowed
student.display()        # ✅ Allowed

# We can also add the attribute from outside the class also 

student.gender = 'male'
print(student.gender)
