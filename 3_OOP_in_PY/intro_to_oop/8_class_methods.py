# ============================================================
# CLASS METHODS
# ============================================================

# Class methods belong to the class.
#
# They use `cls` as the first parameter.
#
# They are created using @classmethod.
#
# Example:
#
class Student:
    school = "GCUF"

    @classmethod
    def change_school(cls, name):
        cls.school = name

print(Student.school)
Student.change_school("FAST")
print(Student.school)


# self → current object
# cls  → current class
#
# HINT:
# Instance Method → self → object data
# Class Method    → cls  → class data
#
# Easy memory:
# self = Object
# cls  = Class