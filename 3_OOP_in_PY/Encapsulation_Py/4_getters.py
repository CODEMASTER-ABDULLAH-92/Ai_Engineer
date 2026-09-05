# Getters in Python

# A getter is a method used to retrieve (read) the value of a private attribute from a class.

# Getters are commonly used with encapsulation, because they allow controlled access to data that we don't want to access directly.

class Student:
    def __init__(self):
        self.__name = "Abdullah"

    def get_name(self):
        return self.__name


student = Student()

print(student.get_name())



# =====================================================
# 2. Why do we need a getter?
# =====================================================



# Suppose you have:

class BankAccount:
    def __init__(self):
        self.__balance = 50000

# You cannot normally do:

account = BankAccount()

print(account.__balance)  # ❌




# Instead, you create a getter:

class BankAccount:
    def __init__(self):
        self.__balance = 50000

    def get_balance(self):
        return self.__balance


account = BankAccount()

print(account.get_balance())  # ✅

# Output:

# 50000

# The advantage is that the class controls how the data is accessed.