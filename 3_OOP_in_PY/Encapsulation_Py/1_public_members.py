# In OOP (Object-Oriented Programming), a public member is a variable (attribute) or function (method) that can be accessed directly from outside the class.

# In simple words:

# Public = accessible from anywhere, including outside the class.

class Student:
    def __init__(self):
        self.name = "Abdullah"   # Public attribute

    def display(self):           # Public method
        print(self.name)


student = Student()

print(student.name)      # ✅ Allowed
student.display()        # ✅ Allowed
