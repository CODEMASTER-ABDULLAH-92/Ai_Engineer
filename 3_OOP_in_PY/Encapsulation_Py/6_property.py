# Property Decorator in Python

# The @property decorator is used to make a method behave like an attribute.

# It is especially useful with encapsulation, because it allows us to use getters and setters while accessing the data with normal attribute syntax.


# The Problem with Normal Getter

# Without @property, we normally create a getter like this:

class Student:
    
    def __init__(self):
        self.__age = 20
    
    def get_age(self):
        return self.__age

stu = Student()
print(stu.get_age())


# We have to call:
# get_age()
# with parentheses.


# Using @property

# With the @property decorator, we can make the getter behave like an attribute.

class Student:
    
    def __init__(self):
        self.__age = 20
    @property
    def age(self):
        return self.__age

stu = Student()
print(stu.age)


# Property with a Setter

# The really useful part is that we can use @property together with a setter.


class Student:
    def __init__(self):
        self.__age = 20

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")


student = Student()

# Getter
print(student.age)

# Setter
student.age = 25

# Getter
print(student.age)



# ===============================================
# Important Syntax
# ===============================================

# The basic syntax is:

# ==============================================
# Getter
# ==============================================


@property
def attribute(self):
    return self.__attribute
            



# ==============================================
# Setter
# ==============================================

@attribute.setter
def attribute(self, value):
    self.__attribute = value

# Notice that the setter uses the same name as the property:



class BankAccount:

    def __init__(self, balance):
        # Private attribute
        self.__balance = balance

    # Getter
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, balance):

        # Validate the balance
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


account = BankAccount(50000)

# Getter
print(account.balance)

# Setter
account.balance = 75000

# Getter
print(account.balance)
