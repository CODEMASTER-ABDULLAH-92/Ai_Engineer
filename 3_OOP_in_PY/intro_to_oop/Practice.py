# Q1. Student Information
# Create a Student class with instance variables:

# name
# age
# marks

# Create two objects with different values and print their information.

def oop():
    class Student:
        def __init__(self, name, age,marks):
            self.name = name
            self.age = age
            self.marks = marks
        
        def show_details(self):
            print(self.name, self.marks,self.age)
    s1 = Student("Muhammad Abdullah", 21, 1082)
    s2 = Student("Muhammad Abdullah", 18, 751)

    s1.show_details()
    s2.show_details()

# oop()


# Q2. Bank Account
# Create an Account class with:

# account_holder
# balance

# Create two accounts and show that each object has its own balance.

def oop():
    class Account:
        
        def __init__(self, account_holder, balance):
            self.account_holder = account_holder
            self.balance = balance
        
        def show_details(self):
            print("Account Holder Name: ", self.account_holder, "Balance: ", self.balance, '\n')
            

    a1 = Account("Muhammad Abdullah", 2000)
    a2 = Account("Rajab Ali", 3000)

    a1.show_details()
    a2.show_details()

# oop()


# Q3. Change Instance Variable
# Create a Car class with an instance variable color. Create two cars with different colors. Change the color of only the first car and print both colors.


def oop():
    class Car:
        def __init__(self, color):
            self.color = color
        
        def showDetails(self):
            print("Car Color:", self.color)
    
    c1 = Car("Black")
    c2 = Car("Red")
    
    print("Before changing color:")
    c1.showDetails()
    c2.showDetails()
    
    # Change color of only the first car
    c1.color = "Blue"  # or c1.color = "White"
    
    print("\nAfter changing color of first car:")
    c1.showDetails()
    c2.showDetails()

# oop()


# Second method

def oop():
    class Car:
        def __init__(self, color):
            self.color = color
        
        def showDetails(self):
            print("Car Color:", self.color)
        
        def changeColor(self, new_Color):
            self.color = new_Color
            
    c1 = Car("Black")
    c2 = Car("Red")
    
    print("Before changing color:")
    c1.showDetails()
    c2.showDetails()
    
    c2.changeColor("White")
    
    print("\nAfter changing color of first car:")
    c1.showDetails()
    c2.showDetails()

# oop()       



# =============================================
# Class Variables Questions 
# =============================================

# Q4. School Name

# Create a Student class with a class variable:
# school = "ABC School"
# Create three students and print their school name.

def oop():
    class Student:
        school = "ABC School"  # Single class variable shared by all instances
        
        def __init__(self, name):
            self.name = name

    # Create three students
    s1 = Student("Ali")
    s2 = Student("Ahmed")
    s3 = Student("Sara")

    # Print school name for each student
    print(f"{s1.name} studies at: {s1.school}")
    print(f"{s2.name} studies at: {s2.school}")
    print(f"{s3.name} studies at: {s3.school}")

# oop()


# Q5. Change Class Variable
# Create an Employee class with:

# company = "Google"

# Create two employees. Change the company using the class and show that both employees see the new value.

def oop():
    class Employee:
        company = "Google"  # Class variable
        
        def __init__(self, name):
            self.name = name

    E1 = Employee("Abdullah")
    E2 = Employee("Rajab")

    print("Before changing company:")
    print(f"{E1.name} works at: {E1.company}")
    print(f"{E2.name} works at: {E2.company}")

    # Change class variable
    Employee.company = "MicroSoft"

    print("\nAfter changing company:")
    print(f"{E1.name} works at: {E1.company}")
    print(f"{E2.name} works at: {E2.company}")

    E1.company = "Amazon"  # This creates an instance variable, not changing class variable
    Employee.company = "Apple"  # This changes the class variable for ALL instances

# oop()

# Q6. Instance vs Class Variable
# Create a Student class with:
# --> class variable --> school = "ABC"
# and an instance variable:
#  --> name
# Create two students and demonstrate that name is different but school is shared.

def oop():
    class Student:
        
        school = "GCUF"
        
        def __init__(self, name):
            self.name = name
        
        def showDetails(self):
            print(f'Name: {self.name}\nSchool: {self.school}')
    s1 = Student("Muhammad Abdullah")
    s2 = Student("Rajab Ali")
    s1.showDetails()
    s2.showDetails()

# oop()


# =====================================
# 3. Instance Methods
# =====================================

# Q7. Student Introduction
# Create a Student class with name and age. Create an instance method:

# introduce()

# that prints:

# My name is Ali
# My age is 20


def oop():
    class Student:
        def __init__(self, name,age):
            self.name = name
            self.age = age
        
        def show_details(self):
            print(f'My name is {self.name}\nMy age is {self.age}')
    
    s1 = Student("Muhammad Abdullah", 21)
    s1.show_details()

# oop()


# Q8. Rectangle
# Create a Rectangle class with length and width.

# Create instance methods:

# area()
# perimeter()

# Print both values.

def oop():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width
        
        def area(self):
            return self.width * self.length  # Return instead of print
        
        def perimeter(self):
            return 2 * (self.length + self.width)  # Return instead of print

    rect = Rectangle(4, 5)
    print(f'Area of Rectangle: {rect.area()}')
    print(f'Perimeter of Rectangle: {rect.perimeter()}')

# oop()


# Q9. Counter
# Create a Counter class with an instance variable count = 0.

# Create an instance method:

# increment()

# that increases the count by 1.

# Call it five times and print the final count.

def oop():
    class Counter:
        
        def __init__(self, count):
            self.count = count
            
        def increment(self):
            self.count += 1 
            return self.count

    c = Counter(0)
    for i in range(5):
        c.increment()
    print(c.count)
# oop()

# =======================================
# 4. Class Methods
# =======================================

# Q10. Change Company
# Create an Employee class with a class variable:

# company = "ABC"

# Create a class method:

# change_company()

# that changes the company name.

def oop():
    
    class Employee:
        company = "ABC"
        
        @classmethod
        def change_company(cls, new_company):
            cls.company = new_company
        
        @classmethod
        def show_company(cls):
            print(cls.company)

    # Create an instance
    E1 = Employee()  # ← Added parentheses

    # Change company using class method
    E1.change_company("MicroSoft")
    E1.show_company()  # Output: MicroSoft

# oop()


# Q11. Count Objects
# Create a class Student with a class variable:

# total_students = 0

# Every time a new Student object is created, increase total_students.

# Create five students and print:

# Total Students: 5

def oop():
    class Student:
        
        total_students = 0
        
        def __init__(self, name):
            self.name = name
            Student.total_students +=1
        
        @classmethod
        def display(cls):
            print(f"Total students: {cls.total_students}")

    S1 = Student("A")
    S2 = Student("B")
    S3 = Student("C")
    S4 = Student("D")
    S5 = Student("E")
    S5.display()

# oop()


# Q12. Alternative Constructor
# Create a Person class with name and age.

# Create a class method:

# from_string()

# that takes:

# "Ali,20"

# and creates a Person object from it.

# This is a slightly more advanced and very useful use of @classmethod.

def oop():
    class Person:
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        @classmethod
        def from_string(cls, data):
            name, age = data.split(",")
            return cls(name, int(age))


    P = Person.from_string("Ali,20")

    print(P.name)
    print(P.age)

# oop()

# ==============================
# Static Methods
# ==============================


# Q13. Even Checker
# Create a Number class with a static method:

# is_even(number)

# It should return True if the number is even and False otherwise.

def oop():
    class Number:
        
        @staticmethod
        def is_even(number):
            if number % 2 == 0:
                return True
            else:
                return False


    N = Number()

    result = N.is_even(20)
    print(result)

# oop()

# Q14. Calculator
# Create a Calculator class with static methods:

# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)

# Call them without creating an object.

def oop():
    class Calculator:
        
        @staticmethod
        def add(a, b):
            return a + b
        
        @staticmethod
        def subtract(a, b):
            return a - b
        
        @staticmethod
        def multiply(a, b):
            return a * b
        
        @staticmethod
        def divide(a, b):
            return a / b


    print(Calculator.add(12, 3))
    print(Calculator.subtract(12, 3))
    print(Calculator.multiply(12, 3))
    print(Calculator.divide(12, 3))

# oop()


# Q15. Utility Method
# Create a MathUtils class with static methods:

# is_prime(n)
# is_palindrome(n)

# Neither method should use self or cls.

def oop():
    class MathUtils:

        @staticmethod
        def is_prime(number):
            if number <= 1:
                return False

            for i in range(2, number):
                if number % i == 0:
                    return False

            return True

        @staticmethod
        def is_palindrome(number):
            reversed_num = 0
            temp = number

            while number > 0:
                digit = number % 10
                reversed_num = reversed_num * 10 + digit
                number = number // 10

            return temp == reversed_num


    print(MathUtils.is_prime(7))
    print(MathUtils.is_prime(10))

    print(MathUtils.is_palindrome(121))
    print(MathUtils.is_palindrome(123))

# oop()

# Employee System

# Create an Employee class with:

# Instance variables: name, salary
# Class variable: company
# Instance method: display()
# Class method: change_company()
# Static method: is_valid_salary()

# Test all of them.
def oop():
    class Employee:

        company = "Google"

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        # Instance method
        def display(self):
            print(f"Name: {self.name}")
            print(f"Salary: {self.salary}")

        # Class method
        @classmethod
        def change_company(cls, new_company):
            cls.company = new_company

        # Static method
        @staticmethod
        def is_valid_salary(salary):
            return salary >= 0


    # Create object
    E = Employee("Muhammad Abdullah", 10000)

    # Instance method
    E.display()

    # Class variable
    print(E.company)

    # Class method
    E.change_company("Microsoft")
    print(E.company)

    # Static method
    print(Employee.is_valid_salary(1000))
    print(Employee.is_valid_salary(-500))

# oop()


# Q23. Bank Account

# Create a BankAccount class with:

# owner
# balance
# class variable bank_name

# Methods:

# deposit()
# withdraw()
# display_balance()

# Add a class method:

# change_bank_name()

# Add a static method:

# is_valid_amount()


def oop():
    class BankAccount:

        bank_name = "MCB"

        def __init__(self, owner, balance):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            if BankAccount.is_valid_amount(amount):
                self.balance += amount
                return self.balance
            return "Invalid amount"

        def withdraw(self, amount):
            if not BankAccount.is_valid_amount(amount):
                return "Invalid amount"

            if amount > self.balance:
                return "Insufficient balance"

            self.balance -= amount
            return self.balance

        def display_balance(self):
            print(f"Balance: {self.balance}")

        @classmethod
        def change_bank_name(cls, new_bank_name):
            cls.bank_name = new_bank_name

        @staticmethod
        def is_valid_amount(amount):
            return amount > 0


    B = BankAccount("Abdullah", 2000)

    B.deposit(1000)
    B.display_balance()

    B.withdraw(500)
    B.display_balance()

    B.change_bank_name("UBL")
    print(B.bank_name)

    print(B.is_valid_amount(0))
    print(B.is_valid_amount(500))

# oop()



# Q24. Student Management

# Create a Student class with:

# Instance variables:
# name
# marks

# Class variable:
# school

# Instance method:
# display()

# Class method:
# change_school()

# Static method:
# is_pass(marks)

# Create three students and demonstrate all three types of methods.

def oop():
    class Student:
        
        school = "GCUF"
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks
        
        
        def display(self):
            print(f"Name: {self.name}\nMarks: {self.marks}")
        
        @classmethod
        def change_school(cls,new_school):
            cls.school = new_school
        
        @staticmethod
        def is_pass(marks):
            if marks >=33:
                print("Pass")
            else:
                print("Fail")

    S =Student("Muhammad Abdullah", 1082)
    S.display()
    S.change_school("WAU")
    S.is_pass(78)
    
oop()

