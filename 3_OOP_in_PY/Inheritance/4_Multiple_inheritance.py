# Multiple Inheritance in Python OOP

# Multiple inheritance means that one child class inherits from two or more parent classes.

# =======================
# Basic Syntax:
# =======================

    
class Parent1:
    # methods and attributes
    pass


class Parent2:
    # methods and attributes
    pass


class Child(Parent1, Parent2):
    # methods and attributes
    pass




class Father:

    def work(self):
        print("Father is working")


class Mother:

    def cook(self):
        print("Mother is cooking")


class Child(Father, Mother):
    pass


child = Child()

child.work()
child.cook()


