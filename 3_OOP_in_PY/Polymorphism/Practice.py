# =========================================
## 1. Method Overriding
# =========================================

# Q1. Animal Sounds
# Create a parent class `Animal` with:

# make_sound():
# Create two child classes:

# Animal
#  /   \
# Dog   Cat
# 
# Override `make_sound()` in both classes.
# Expected behavior:

# 
# Dog → Bark
# Cat → Meow
def oop():

    class Animal:
        pass


    class Dog(Animal):
        def make_sound(self):
            print("Bark")


    class Cat(Animal):
        def make_sound(self):
            print("Meow")


    cat = Cat()
    dog = Dog()

    cat.make_sound()
    dog.make_sound()

# oop()

# ---

# =============================================
# # 3. Operator Overloading
# =============================================

# # Q7. Add Two Objects

# Create a `Point` class:


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# 

# Overload `+` so:


# p1 = Point(2, 3)
# p2 = Point(4, 5)

# p3 = p1 + p2
# 

# produces:

# 
# x = 6
# y = 8

def oop():

    class Point:
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

    p1 = Point(5, 5)
    p2 = Point(5, 10)

    p3 = p1 + p2

    print(p3.x)
    print(p3.y)

# oop()




# # Q8. Compare Objects Using `==`

# Create a `Student` class with:

# 
# name
# age
# 

# Use operator overloading so:


# student1 == student2
# returns `True` when both students have the same data.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, value):
        return self.name == value.name and self.age == value.age


stu = Student("Rajab", 23)
stu2 = Student("Rajab", 23)

stu3 = stu == stu2
print(stu3)

# # Q9. Subtract Objects

# Create a `Vector` class:


# x
# y
# 

# Overload `-` so:


# v1 - v2
# 

# returns a new vector.

def oop():

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __sub__(self, other):
            x = self.x - other.x
            y = self.y - other.y

            return Vector(x, y)


    v1 = Vector(5, 10)
    v2 = Vector(5, 10)

    v3 = v1 - v2

    print(v3.x)
    print(v3.y)

# oop()

# ======================================
# # 4. Magic Methods
# ======================================


# # Q10. `__str__()`

# Create a `Student` class:


# class Student:
#     def __init__(self, name, age):
#         ...

# Implement:
# __str__()

# so:
# student = Student("Ali", 20)
# print(student)

# produces something like:
# Student: Ali, Age: 20

def oop():
    class Student:
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __str__(self):
            return f"Student: {self.name} Age: {self.age}"

    student = Student("Ali", 20)
    print(student)

# oop()




# # Q11. `__len__()`
# Create a `Playlist` class containing a list of songs.

# Implement:
# __len__()

# so:
# playlist = Playlist(["Song A", "Song B", "Song C"])
# print(len(playlist))
# returns:
# 3

def oop():

    class Playlist:
        def __init__(self, songs):
            self.songs = songs

        def __len__(self):
            return len(self.songs)


    playlist = Playlist(["Song A", "Song B", "Song C"])

    print(len(playlist))

# oop()
# ---


# # Q13. Multiple Magic Methods

# Create a `Book` class and implement:
# __str__()
# __len__()
# __eq__()

# Then test:
# print(book)
# len(book)
# book1 == book2

def oop():
    class Book:

        def __init__(self, title):
            self.title = title

        def __str__(self):
            return f"Book: {self.title}"

        def __len__(self):
            return len(self.title)

        def __eq__(self, other):
            return self.title == other.title


    book1 = Book("Can't Hurt Me")
    book2 = Book("Can't Hurt Me")
    book3 = Book("Never Finished")

    print(book1)
    print(len(book1))
    print(book1 == book2)
    print(book1 == book3)

# oop()

