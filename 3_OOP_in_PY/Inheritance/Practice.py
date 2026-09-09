# ===========================
# 1. Parent Class — Base Class

# # Q1. Animal

# Create an `Animal` class with:


# name
# age
# 

# Create an object and print its information.

def oop():
    class Animal:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
        
        def display_info(self):
            return f"Name: {self.__name}, Age: {self.__age}"

    animal = Animal("Cix", 1)
    print(animal.display_info())

# oop()


# # Q2. Vehicle
# Create a parent class `Vehicle` with a method:

# start()

# that prints: 
# Vehicle started

def oop():
    class Vehicle:
        
        @staticmethod #if you don't need instance data, like self, cls use the static method 
        def start():
            print("Vehicle Started: ")

    v = Vehicle()
    v.start()
    
# oop()


# ======================================================
# ## 2. Child Class — Derived Class
# ======================================================


# # Q3. Dog inherits Animal
# Create:
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# 

# Create a `Dog` class that inherits from `Animal`.
# Create a `Dog` object and call:
# dog.eat()

def oop():
    class Animal:
        
        def eat(self):
            print("Animal is eating")

    class Dog(Animal):
        pass

    dog = Dog()
    dog.eat()
# oop()



# # Q4. Child's Own Method
# Create a parent class `Animal` with `eat()`.
# Create a child class `Dog` with:

# bark()
# Call both methods using the `Dog` object.

def oop():
    class Animal:
        
        def eat(self):
            print("Animal is eating.")

    class Dog(Animal):
        
        def bark(self):
            print("Dog is barking.")

    dog = Dog()
    dog.eat()
    dog.bark()
        
# oop()

# ==============================================
# 3. Single Inheritance
# ==============================================


# # Q5. Person → Student
# Create:
# Person Class
# Student Class

# `Person` should contain:

# name
# age
# display_person()


# `Student` should contain:
# marks
# display_student()
# 

# Create a `Student` object and access all three pieces of information.

def oop():
    class Person:
        
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
        
        def display_person(self):
            print(f'Name: {self.__name}\nAge: {self.__age}')

    class Student(Person):
        
        def __init__(self, name, age, marks):
            super().__init__(name, age)
            self.__marks = marks
        
        def display_student(self):
            print(f'Marks: {self.__marks}')

    stu = Student("Muhammad Abdullah", 23, 1082)
    stu.display_person()
    stu.display_student()

# oop()


# # Q6. Vehicle → Car

# Create:
# Vehicle
#    ↓
# Car


# Parent:
# start()


# Child:
# drive()


# Call both methods using a `Car` object.

def oop():
    class Vehicle:
        
        @staticmethod
        def start():
            print("Vehicle started.")

    class Car(Vehicle):
        
        @staticmethod
        def drive():
            print("Car is driving")

    car = Car()
    car.start()
    car.drive()

# oop()


# ==========================================
# # 4. Multiple Inheritance
# ==========================================


# # Q7. Father + Mother → Child

# Create:
 
# Father
#   + 
# Mother
#    ↓
#  Child

# Father Class:
# father_method()


# Mother class:
# mother_method()


# `Child` should inherit from both.
# Call both methods using the `Child` object.

def oop():
        
    class Father:
        
        @staticmethod
        def father_method():
            print("Father is Working")
        

    class Mother:
        
        @staticmethod
        def mother_method():
            print("Mother is cooking")

    class Child(Father, Mother):
        pass

    child = Child()
    child.father_method()
    child.mother_method()

# oop()




# # Q8. Multiple Features

# Create:
# class Camera:
#     def take_photo(self):
#         ...

# class Phone:
#     def make_call(self):
#         ...

# class Smartphone(Camera, Phone):
#     ...
# 

# Create a `Smartphone` object and call both methods.

def oop():
    class Camera:
        def take_photo(self):
            print("Photo taken")

    class Phone:
        def make_call(self):
            print("Calling...")

    class Smartphone(Camera, Phone):
        pass

# Create Smartphone object and call both methods
    smartphone = Smartphone()
    smartphone.take_photo()  # Output: Photo taken
    smartphone.make_call()   # Output: Calling...

# oop()


# ======================================
# # 5. Multilevel Inheritance
# ======================================


# # Q9. Animal → Mammal → Dog

# Create:
# Animal
#    ↓
# Mammal
#    ↓
# Dog


# `Animal`:
# eat()

# `Mammal`:
# walk()

# `Dog`:
# bark()
#

# Create a `Dog` object and call all three methods.


def oop():
    class Animal:
        
        def eat(self):
            print("Animal Eat.")

    class Mammal(Animal):
        
        def walk(self):
            print("Mammal Walk.")

    class Dog(Mammal):
        
        def bark(self):
            print("Dog Bark.")

    dog = Dog()
    dog.eat()
    dog.walk()
    dog.bark()

# oop()


# # Q10. Person → Employee → Manager
# Create:

# Person
#    ↓
# Employee
#    ↓
# Manager

# Each class should have one method.

# Create a `Manager` object and call all inherited methods.

def oop():
        
    class Person:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
        
        def display_person(self):
            print(f'Name: {self.__name}\nAge: {self.__age}')

    class Employee(Person):
        def __init__(self, name, age, department):
            super().__init__(name, age)  # ✅ Fixed: Added parentheses
            self.__department = department
        
        def show_department(self):
            print(f'Department: {self.__department}')

    class Manager(Employee):
        def __init__(self, name, age, department, salary):
            super().__init__(name, age, department)  # ✅ Fixed: Added parentheses
            self.__salary = salary
        
        def show_salary(self):
            print(f'Salary: {self.__salary}')

    # Create Manager object and call all methods
    manager = Manager("Abdullah", 23, 'CS', 1000)
    manager.display_person()
    manager.show_department()
    manager.show_salary()

# oop()


# ====================================================
# # 6. Hierarchical Inheritance
# ====================================================

# # Q11. Animal → Dog & Cat
# Create:

#         Animal
#         /    \
#       Dog    Cat
# 

# Parent:
# eat()

# `Dog`:
# bark()

# `Cat`:
# meow()
# Create one `Dog` and one `Cat` object.

def oop():
        
    class Animal:
        def eat(self):
            print("Animal is eating")

    class Dog(Animal):
        def bark(self):           
            print("Dog is barking")

    class Cat(Animal):
        def meow(self):
            print("Cat is meowing")

    # Create Dog and Cat objects
    dog = Dog()
    cat = Cat()

    # Call methods
    dog.eat()    # From Animal
    dog.bark()   # From Dog

    cat.eat()    # From Animal
    cat.meow()   # From Cat
# oop()


# # Q12. Shape → Circle & Rectangle

# Create:

# 
#        Shape
#        /   \
#    Circle Rectangle
# 

# Parent:
# display()

# Circle:
# area()

# Rectangle:
# area()

# Create both objects.

def oop():
    class Shape:
        def display(self):
            print("Here the explanation of the shapes")

    class Circle(Shape):
        def area(self):  # ✅ Changed from circle() to area()
            print("Circle area: πr²")

    class Rectangle(Shape):
        def area(self):  # ✅ Changed from rectangle() to area()
            print("Rectangle area: length × width")

    # Create both objects
    circle = Circle()
    rectangle = Rectangle()

    # Call methods
    circle.display()
    circle.area()

    rectangle.display()
    rectangle.area()

# oop()



# ====================================
# # 8. `super()`
# ====================================



# # Q15. Basic `super()`

# Create:
# class Parent:
#     def show(self):
#         print("Parent")
# 

# Create a child class that overrides `show()` but uses:


# super().show()
# 

# Then print:

# 
# Parent
# Child

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()  # Fixed: Added parentheses
        print("Child")

# Create objects
parent = Parent()
child = Child()

# Call methods
child.show()


# # Q16. `super()` with `__init__`
# Create:
# class Person:
#     def __init__(self, name):
#         self.name = name

# Create a child class `Student` with:
# age

# Use:
# super().__init__(name)

# so both `name` and `age` are initialized.

def oop():
    
    class Person:
        def __init__(self, name):
            self.name = name


    class Student(Person):
        def __init__(self, name,age):
            super().__init__(name)
            self.age = age
        
        def display(self):
            print(f'Name: {self.name}\nAge: {self.age}')

    stu = Student("Abdullah", 23)
    stu.display()
# oop()
    




# ## Q18. School System

# Create:
 
# Person
#   ↓
# Student

# Use:

# * Parent instance variables
# * Child instance variables
# * Parent method
# * Child method
# * `super()`

# Create a student and display all information.
def oop():

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age 
        
        def display_person(self):
            print(f'Name: {self.name}')
            print(f'Age: {self.age}')
        
    class Student(Person):
        def __init__(self, name, age, marks):
            super().__init__(name, age)  # ✅ Using super() for parent init
            self.marks = marks           # ✅ Child instance variable
        
        def display_student(self):       # ✅ Child method
            self.display_person()        # ✅ Calling parent method
            print(f'Marks: {self.marks}') # ✅ Displaying child data

    # Create student object
    stu = Student("Muhammad Abdullah", 23, 1082)

    # Display all information
    stu.display_student()

# oop()



# # Q24. Full Inheritance Project

# Create a small **University Management System**:

# 
# Person
#  ├── Student
#  └── Teacher
# 

# Use:

# * Parent class
# * Child classes
# * Hierarchical inheritance
# * Instance variables
# * Instance methods
# * `super()`

# Then add another level:

# 
# Person
#    ↓
# Student
#    ↓
# GraduateStudent

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        
    def display(self):
        super().display()
        print(f"Marks: {self.marks}")

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)   
        self.salary = salary
    
    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

# ✅ NEW: GraduateStudent inherits from Student
class GraduateStudent(Student):
    def __init__(self, name, age, marks, research_topic):
        super().__init__(name, age, marks)  # Call Student's __init__
        self.research_topic = research_topic
    
    def display(self):
        super().display()  # Calls Student's display (which calls Person's display)
        print(f"Research Topic: {self.research_topic}")

# ============================================
# Test the System
# ============================================

print("=" * 40)
print("UNIVERSITY MANAGEMENT SYSTEM")
print("=" * 40)

# Create Student
print("\n--- STUDENT ---")
student = Student("Alice", 20, 85)
student.display()

# Create Teacher
print("\n--- TEACHER ---")
teacher = Teacher("Dr. Smith", 45, 75000)
teacher.display()

# Create GraduateStudent
print("\n--- GRADUATE STUDENT ---")
grad = GraduateStudent("Bob", 25, 92, "Machine Learning")
grad.display()