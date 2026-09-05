# Private Members in Python

# A private member is a class member that is intended to be accessed only from inside the class.

# In Python, we indicate a private member by using two underscores (__) before its name.


class Student:
    def __init__(self):
        self.name = "Abdullah"          # Public
        self._age = 20                  # Protected
        self.__password = "12345"       # Private

    def show_password(self):
        print(self.__password)


student = Student()

print(student.name)          # ✅ Public
print(student._age)          # ⚠️ Protected (works, but discouraged)
print(student.__password)    # ❌ Cannot access directly
