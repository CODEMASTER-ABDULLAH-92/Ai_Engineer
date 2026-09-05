# Instance Method
#
# - Belongs to an object/instance.
# - First parameter is `self`.
# - Can access instance variables using `self`.
#
# Example:
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):       # Instance Method
#         print(self.name)
#
# student1 = Student("Ali")
# student1.introduce()
#
# Easy rule:
# self + method inside class = Instance Method