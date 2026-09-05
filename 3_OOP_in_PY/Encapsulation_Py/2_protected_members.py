# ============================================
# PROTECTED MEMBERS IN PYTHON
# ============================================

# What They REALLY Are:
# ----------------------
# A protected member in Python is a CONVENTION - not a strict rule.
# It indicates that a member is intended for:
#   ✅ Internal use within the class
#   ✅ Access in child/subclasses
#   ⚠️ Should NOT be accessed directly from outside (but Python still allows it!)

# In Python, we indicate a protected member by using one underscore (_) before its name.


# ============================================
# KEY UNDERSTANDING
# ============================================

# Unlike Java/C++ where 'protected' is ENFORCED, in Python it's a 
# GENTLE WARNING to other developers: 
# "This is for internal use. Access at your own risk!"


# ============================================
# EXAMPLE 1: Basic Protected Member
# ============================================

class Student:
    def __init__(self, name):
        self._name = name  # Protected by convention
    
    def display(self):
        print(f'Name: {self._name}')

# Access within class - ✅ OK
Stu = Student("Abdullah")
Stu.display()  # Output: Name: Abdullah

# Access from outside - ⚠️ Allowed but DISCOURAGED
print(Stu._name)  # Output: Abdullah (still works!)


# ============================================
# EXAMPLE 2: Access in Child Class
# ============================================

class Student:
    def __init__(self):
        self._age = 20  # Protected member

class Child(Student):
    def show(self):
        print(self._age)  # ✅ Accessible in child class (as intended)

# This follows the convention - ✅ OK
student = Child()
student.show()  # Output: 20

# Still accessible from outside - ⚠️ DISCOURAGED
print(student._age)  # Output: 20 (still works!)


# ============================================
# EXAMPLE 3: Why It's Called "Protected"
# ============================================

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected - shouldn't be touched directly
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance

acc = BankAccount(1000)

# ✅ Good practice - using methods
acc.deposit(500)
print(acc.get_balance())  # Output: 1500

# ⚠️ Bad practice - direct access (but Python allows it!)
acc._balance = -999999  # No error! This is why it's only a convention
print(acc._balance)  # Output: -999999 (broken data!)


# ============================================
# COMPARISON TABLE (As Comments)
# ============================================

# Aspect              | Python _variable    | Java/C++ protected
# --------------------|---------------------|-------------------
# Meaning             | "Please don't touch"| "You cannot touch"
# Access from outside | ✅ Allowed (discouraged)| ❌ Not allowed
# Access in child     | ✅ Allowed          | ✅ Allowed
# Enforced by language| ❌ No               | ✅ Yes
# Philosophy          | "We're all consenting adults" | "Protect from mistakes"


# ============================================
# THE GOLDEN RULE
# ============================================

# Protected in Python = Protection by Convention, not by Compulsion

# The underscore _ is like a "Handle with Care" sticker - 
# it warns you, but doesn't stop you!


# ============================================
# IMPORTANT REMINDER
# ============================================

# Your original notes were incorrect because they implied 
# Python ENFORCES protection. Python DOES NOT enforce it - 
# it's just a convention!