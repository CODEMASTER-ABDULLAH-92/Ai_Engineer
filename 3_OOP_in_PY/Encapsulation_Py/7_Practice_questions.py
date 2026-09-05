# =============================================
#  1. Public Members — `variable`
# =============================================

# Q1. Student

# Create a `Student` class with a public variable:
# name

# Create an object and directly access and modify `name`.

# 
# Expected:
# Original Name: Ali
# Updated Name: Ahmed
# 
def oop():

    class Student:
        
        def __init__(self, name):
            self.name = name
            
        def display(self):
            print(f'Name: {self.name}')

    stu = Student("Muhammad Abdullah")
    stu.display()
    stu.name = "Ahmed"
    stu.display()
    
# oop()




#  Q2. Bank Account

# Create an `Account` class with a public variable:


# balance
# 

# Create an account and directly change the balance from outside the class.

# **Goal:** Understand unrestricted public access.

# ---

def oop():
    class Bank:
        def __init__(self, balance):
            self.balance = balance  # public variable

    # Create an account
    B = Bank(1000)  # Note: integer, not string

    # Directly change balance from outside the class
    B.balance = 2000  # Direct access and modification

    # Verify the change
    print(B.balance)  # Output: 2000

# oop()






# =============================================
# # 2. Protected Members — `_variable`
# =============================================



#  Q3. Employee

# Create an `Employee` class with:


# _name
# _salary
# 

# Create a method `display()` that prints both values.

# Access `_name` and `_salary` from outside the class and observe tha still allows it.


def oop():
    class Employee:
        
        def __init__(self, name, salary):
            self._name = name
            self._salary = salary
        
        def display(self):
            print(f'Name: {self._name}\nSalary:{self._salary}')
    E = Employee("Abdullah", 10000)
    E.display()
    print(E._name)
    print(E._salary)

# oop()

#  Q4. Protected Variable Modification

# Create:


# class Student:
#     def __init__(self, marks):
#         self._marks = marks
# 

# Modify `_marks` from outside the class.

# Question: Why is `_marks` called protected even through allows direct access?

# ---

def oop():
    class Student:
        def __init__(self, marks):
            self._marks = marks
        
    stu = Student(1000)
    stu._marks = 2000
    print(stu._marks)

# Key Points:
# Convention, not Enforcement: In Python, the single underscore _ is a naming convention that signals to other developers: "This is for internal use. Don't touch it unless you know what you're doing."

# "We're all consenting adults": Python follows this philosophy - it trusts programmers to respect conventions rather than enforcing strict access control like Java or C++.

# Protected means "protected by convention": Unlike other languages where protected actually prevents access, in Python it's a warning label, not a lock.


# oop()


# ===========================================================
# # 3. Private Members — `__variable`
# ===========================================================

#  Q5. Bank Account
# Create an `Account` class with:
# __balance

# Create methods:
 
# show_balance()
# deposit()

# Try accessing:

# account.__balance
# from outside the class.
# Observe what happens.

def oop():
    class Bank:
        def __init__(self, balance):
            self.__balance = balance  # Private attribute (name mangling)
        
        def show_balance(self):
            print(f'Balance: {self.__balance}')
        
        def deposit(self, amount):  # Fixed parameter name
            if amount <= 0:
                print("Amount must be greater than zero")
            else:
                self.__balance += amount

    account = Bank(1000)
    account.show_balance()        # Output: Balance: 1000
    account.deposit(2000)         # Output: Balance: 3000
    account.show_balance()        # Output: Balance: 3000

    # Try to access private attribute directly
    print(account.__balance)      # ❌ AttributeError!

    # But you CAN access it using name mangling (NOT recommended!)
    print(account._Bank__balance)  # ⚠️ Output: 3000 (works but DON'T do this!)

# oop()

#  Q6. Private Password

# Create a `User` class with:
 
# __password

# Create: 
# show_password()

# and try to access the password directly from outside the class.

def oop():
    class User:
        
        def __init__(self, password):
            self.__password = password  # Private attribute (name mangling)
        
        def show_password(self):
            return self.__password  # Access through method

    user = User("abdullah123")

    # ✅ Correct way - using the method
    print(user.show_password())  # Output: abdullah123

    # ❌ Wrong way - direct access (will raise error)
    print(user.__password)  # ❌ AttributeError!

# oop()

# =========================================
#  5. Getters — Reading Data
# =========================================

# Create a `Student` class with private:
# __marks

# Create:
# get_marks()
# that returns the marks.

# Use:
# student.get_marks()
# to read the private variable.

def oop():
    class Student:
        def __init__(self, marks):
            self.__marks = marks  # Private attribute
        
        def get_marks(self):      # 👈 This is a GETTER method
            return self.__marks   # Returns private value

    stu = Student(1083)
    print(stu.get_marks())  # ✅ Using getter to access private data
# oop()



#  Q10. Bank Balance Getter

# Create:

# class Account:
#     __balance = 5000
# 

# Create:
 
# get_balance()

# Print the balance using the getter.

def oop():
    class Account:
        
        def __init__(self, balance):
            self.__balance = balance
        
        def get_balance(self):
            return self.__balance
        
    account = Account(1000)
    balance = account.get_balance()
    print(balance)

# oop()



# =========================================
# # 6. Setters — Writing Data
# =========================================


#  Q11. Student Marks Setter
# Create a `Student` class with:

# __marks

# Create:
# set_marks(marks)
# that changes the marks.

# Test:
# Old marks → 70
# New marks → 85

def oop():
    class Student:
        
        def __init__(self, marks):
            self.__marks = marks
        
        def set_marks(self, marks):
            self.__marks = marks
        
        def get_marks(self):
            return self.__marks


    stu = Student(70)

    print("Old marks:", stu.get_marks())

    stu.set_marks(85)

    print("New marks:", stu.get_marks())

# oop()

#  Q12. Controlled Age Update

# Create a `Person` class with private:
# __age

# Create:
# set_age(age)
# Allow the age to change only if it is greater than `0`.

def oop():
    class Person:
    
        def __init__(self, age):
            self.__age = age
        
        def set_age(self, age):
            if age > 0:
                self.__age = age


    person = Person(23)
    person.set_age(30)

# oop()


# ==========================================================
# # 7. Property Decorator — `@property`
# ==========================================================


# Create a `Student` class with:
# __name

# Create:
# @property
# def name(self):
#     return self.__name

# Then access it like:
# student.name

# instead of:
# student.get_name()
def oop():
    class Student:
        
        def __init__(self, name):
            self.__name = name
        
        @property
        def name(self):
            return self.__name

    Stu = Student("Abdullah")
    print(Stu.name)

# oop()

#  Q14. Property with Setter

# Create a `Person` class with private:
# __age

# Create: 
# @property
# def age(self):
#     ...

# @age.setter
# def age(self, value):
#     ...
# Then allow:
# person.age = 25
# while keeping `__age` private.

def oop():
    class Person:
    
        def __init__(self, age):
            self.__age = age
        
        @property
        def age(self):
            return self.__age
        
        @age.setter
        def age(self, value):
            if value > 0:
                self.__age = value
            else:
                print("Age must be greater than 0")


    person = Person(23)

    print(person.age)

    person.age = 24
    print(person.age)

    person.age = -5
    print(person.age)

# oop()


# ## Q18. Bank Account

# Create an `Account` class with:
# Private:
# __balance

# Getter:
# get_balance()

# Setter:
# set_balance()

# Methods:
# deposit()
# withdraw()


# Rules:
# deposit amount > 0
# withdraw amount > 0
# withdraw amount <= balance

def oop():
    class Account:

        def __init__(self, balance):
            self.__balance = balance

        @property
        def balance(self):
            return self.__balance

        @balance.setter
        def balance(self, balance):
            self.__balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
            else:
                print("Amount must be greater than 0")

        def withdraw(self, amount):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Please enter a valid amount")


    account = Account(1000)

    print(account.balance)

    account.balance = 2000
    print(account.balance)

    account.deposit(2000)
    print(account.balance)

    account.withdraw(1000)
    print(account.balance)

# oop()


# ## Q19. Student Management

# Create a `Student` class with:

# Private:
# __name
# __marks

# Getter:
# get_name()
# get_marks()

# Setter:
# set_name()
# set_marks()

# Validation:
# marks must be 0–100
# name cannot be empty
# Create two students and test all methods.

def oop():
    class Student:

        def __init__(self, name, marks):
            self.__name = name
            self.__marks = marks

        def get_name(self):
            return self.__name

        def get_marks(self):
            return self.__marks

        def set_name(self, new_name):
            if new_name.strip() != "":
                self.__name = new_name
            else:
                print("Name cannot be empty.")

        def set_marks(self, new_marks):
            if 0 <= new_marks <= 100:
                self.__marks = new_marks
            else:
                print("Marks must be between 0 and 100.")


    # Student 1
    student1 = Student("Abdullah", 85)

    print(student1.get_name())
    print(student1.get_marks())

    student1.set_name("Ali")
    student1.set_marks(90)

    print(student1.get_name())
    print(student1.get_marks())


    # Student 2
    student2 = Student("Ahmed", 75)

    print(student2.get_name())
    print(student2.get_marks())

    student2.set_name("Hamza")
    student2.set_marks(95)

    print(student2.get_name())
    print(student2.get_marks())

# oop()



# ## Q20. Property-Based Student

# Create the same `Student` class, but instead of getters/setters:
# @property
# and:
# @property.setter
# Use:
# student.name
# student.marks

# student.name = "Ali"
# student.marks = 85

# Validate the values inside the setters.

def oop():
    
    class Student:
    
        def __init__(self, name, marks):
            self.__name = name
            self.__marks = marks
        
        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, value):
            if value.strip() != "":
                self.__name = value
            else:
                print("Err")
        
        @property
        def marks(self):
            return self.__marks
        
        @marks.setter
        def marks(self, value):
            if 0 <= value <= 100:
                self.__marks = value
            else:
                print("Err")


    student = Student("Abdullah", 70)

    print(student.name)
    print(student.marks)

    student.name = "Ali"
    student.marks = 85

    print(student.name)
    print(student.marks)
# oop()



#  Q24. Full Encapsulation Project

# Create a `BankAccount` class using:

# * Private members
# * Getter
# * Setter
# * `@property`
# * Validation
# * Instance methods

# Implement:

# deposit()
# withdraw()
# balance
# 

# with proper validation.


def oop():
    class BankAccount:

        def __init__(self, name, password, amount):
            self.__name = name
            self.__password = password

            if amount >= 0:
                self.__amount = amount
            else:
                self.__amount = 0
                print("Initial balance cannot be negative.")

        # Name getter
        @property
        def name(self):
            return self.__name

        # Name setter
        @name.setter
        def name(self, new_name):
            if new_name.strip() != "":
                self.__name = new_name
            else:
                print("Name cannot be empty.")

        # Password getter
        @property
        def password(self):
            return self.__password

        # Password setter
        @password.setter
        def password(self, new_password):
            if new_password.strip() != "":
                self.__password = new_password
            else:
                print("Password cannot be empty.")

        # Balance getter
        @property
        def balance(self):
            return self.__amount

        # Balance setter
        @balance.setter
        def balance(self, new_amount):
            if new_amount >= 0:
                self.__amount = new_amount
            else:
                print("Balance cannot be negative.")

        # Deposit
        def deposit(self, amount):
            if amount > 0:
                self.__amount += amount
            else:
                print("Deposit amount must be greater than 0.")

        # Withdraw
        def withdraw(self, amount):
            if amount > 0 and amount <= self.__amount:
                self.__amount -= amount
            else:
                print("Invalid withdrawal amount or insufficient balance.")
    
    account = BankAccount("Abdullah", "12345", 1000)

    print(account.name)
    print(account.balance)

    account.deposit(500)
    print(account.balance)

    account.withdraw(300)
    print(account.balance)

    account.balance = 5000
    print(account.balance)    

oop()