# ==========================================
# Python If, Elif, and Else Statements
# ==========================================

# ------------------------------------------
# 1. Simple if Statement
# ------------------------------------------

from traceback import print_tb


def program():
    age = 20

    if age >= 18:
        print("You can vote")
# program()

# ------------------------------------------
# 2. if - else Statement
# ------------------------------------------

def program():
    age = 15

    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")
# program()

# ------------------------------------------
# 3. if - elif - else Statement
# ------------------------------------------

def program():
    marks = 75

    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    else:
        print("Grade C")

# program()


"""1. Write a Python program that takes an integer as input and prints "Positive" if the number is greater than 0.
"""

def program():
    value = int(input("Enter the value: "))
    if value > 0:
        print("Positive")

# program()

'''
Write a program that takes a user's age as input and prints "Adult" if the age is 18 or older, otherwise prints "Minor"
'''

def program():
    age = int(input("Enter the age: "))
    if age >= 18:
        print("Adults")
    else:
        print("Minor")

# program()


'''
Write a program that takes a numerical grade (0-100) as input and prints the corresponding letter grade:

A for 90-100
B for 80-89
C for 70-79
F for below 70

'''
def program():
    marks = int(input("Enter the marks: "))
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    else:
        print("D")
# program();




'''
Write a program that takes three numbers as input and prints the largest number using if-elif-else and logical operators (and/or).
'''

def program():
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    num3 = int(input("Enter the num3: "))

    if num1 > num2 and num1 > num3:
        print("Num1 is greater: ")
    elif num2 > num1 and num2 > num3:
        print("Num2 is greater: ")
    else:
        print("Num3 is greater: ")

# program()



'''
Write a program that takes a single character as input and checks if it is a vowel (a, e, i, o, u - case insensitive). Print "Vowel" or "Consonant"
'''

def program():
    character_val = input("Enter the value: ")
    if character_val == 'a' or character_val == 'e' or character_val == 'i' or character_val == 'o' or character_val == 'u' or character_val == 'A' or character_val == 'E' or character_val == 'I' or character_val == 'O' or character_val == 'U':
        print("Vowels")
    else:
        print('Consonant')

# program() 


'''
Better Pythonic Approch is here.
1. lower() converts all uppercase letters to lowercase.
'''

def program():
    val = input("Enter the value ").lower();
    if val in "aeiou":
        print("Vowel")
    else:
        print("Consonent")
# program()


'''
Write a program that takes a year as input and prints "Leap Year" if it is divisible by 400, or if it is divisible by 4 but not by 100.
'''

def program():
    year = int(input("Enter the year: "))
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("Leap Year: ")
    else:
        print("Not a Leap Year")

# program()


'''
Write a single line of code using the ternary operator that assigns the string "Even" to a variable result if a given number is even, else assigns "Odd"
'''

def program():
    val = int(input("Enter the value: "))
    res = "Even" if val % 2 == 0 else "Odd"
    print(res)

# program();




'''
Write a program that simulates a simple login system. Ask the user for a username and password.

If the username is "admin" and password is "1234", print "Access Granted".
If the username is "admin" but password is wrong, print "Invalid Password".
If the username is not "admin", print "Invalid Username".
If both are empty, print "Fields cannot be empty".
'''

def program():
    userName = input("Enter the userName: ")
    password = input("Enter the Password: ")
    if userName == "" or password == "":
        print("Fields cannot be empty")
    elif userName == "admin" and password == "1234":
        print("Access Granted: ")
    elif userName == "admin" and password != '1234':
        print('Invalid Password')
    elif userName != "admin" and password == '1234':
        print('Invalid userName')

# program();



'''
Write a program that determines if a triangle is valid based on three side lengths. A triangle is valid if:

- All sides are positive
- The sum of any two sides is greater than the third side
'''

def program():
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))

    if side1 > 0 and side2 > 0 and side3 > 0 and \
       side1 + side2 > side3 and \
       side1 + side3 > side2 and \
       side2 + side3 > side1:
        print("Triangle")
    else:
        print("Not a triangle")

# program()
