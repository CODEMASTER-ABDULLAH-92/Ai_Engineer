# ================
# String
# ================

# A string is an immutable, ordered sequence of characters. Strings are one of the most fundamental and widely used data types in Python.


# Examples of strings

empty_string = ""
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = '''Multi-line
string'''
multi_line = """Also multi-line
with double quotes"""

# ======================================
# Key Characteristics:
# ======================================

# ✅ Ordered - Characters have a defined order (index starting at 0)
# ✅ Immutable - Cannot be changed after creation
# ✅ Iterable - Can iterate through characters
# ✅ Indexable - Access characters by index (positive and negative)
# ✅ Slicable - Extract substrings using slicing
# ✅ Unicode Support - Can handle any Unicode character


def different_ways():
    # Method 1: Single quotes
    str1 = 'Hello'

    # Method 2: Double quotes
    str2 = "World"

    # Method 3: Triple quotes (multi-line)
    str3 = '''This is a
    multi-line
    string'''

    str4 = """Also
    multi-line"""

    # Method 4: str() constructor
    str5 = str(123)  # '123'
    str6 = str(3.14)  # '3.14'
    str7 = str([1, 2, 3])  # '[1, 2, 3]'

    # Method 5: Using f-strings (formatted)
    name = "Alice"
    str8 = f"Hello, {name}!"  # 'Hello, Alice!'

    # Method 6: Using format()
    str9 = "Hello, {}!".format(name)  # 'Hello, Alice!'

    # Method 7: Concatenation
    str10 = "Hello" + " " + "World"

    # Method 8: Using join()
    str11 = " ".join(["Hello", "World"])

# different_ways()


# ==========================
# Quotes and Escaping
# ==========================

def Quotes_and_Escaping():
    # Using different quotes to avoid escaping
    string1 = "She said 'Hello'"
    string2 = 'He said "Hi"'

    # Using escape sequences
    string3 = "She said \"Hello\""
    string4 = 'He said \'Hi\''

    # Escape sequences
    print("Hello\nWorld")     # New line
    print("Hello\tWorld")     # Tab
    print("Hello\\World")     # Backslash
    print("Hello\bWorld")     # Backspace
    print("Hello\rWorld")     # Carriage return

    # Raw strings (ignore escape sequences)
    raw = r"C:\Users\Name\Documents"
    print(raw)  # C:\Users\Name\Documents

# Quotes_and_Escaping()

# ====================
# slicing 
# ====================


# Slicing [start:end:step]

def slicing():
    text = "Hello World"

    # Basic slicing
    print(text[0:5])   # 'Hello'
    print(text[6:11])  # 'World'
    print(text[6:])    # 'World' (to end)
    print(text[:5])    # 'Hello' (from start)
    print(text[:])     # 'Hello World' (copy)

    # Slicing with step
    print(text[0:11:2])  # 'HloWrd' (every 2nd character)
    print(text[::2])     # 'HloWrd'
    print(text[1:10:2])  # 'el ol'
    print(text[::-1])    # 'dlroW olleH' (reverse)

    # Slicing with negative indices
    print(text[-5:])    # 'World'
    print(text[:-6])    # 'Hello'
    print(text[-6:-1])  # ' Worl'
    print(text[-1:-6:-1])  # 'dlroW'

# slicing()

def basic_example():

    email = "user@example.com"
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print(f"Username: {username}, Domain: {domain}")

# basic_example()


# ======================================
# complete strings methods 
# ======================================

def complete_stings_method():
    text = "  Hello World  "

    print("Straße".casefold())  # 'strasse'
    # casefold() - Aggressive lowercase for case-insensitive matching
    # capitalize() - First letter uppercase, rest lowercase
    print(text.capitalize())  # '  hello world  '

    print("hello world".capitalize())  # 'Hello world'
    # title() - Each word capitalized
    print("hello world".title())  # 'Hello World'

    # lower() - All lowercase
    print(text.lower())  # '  hello world  '

    # upper() - All uppercase
    print(text.upper())  # '  HELLO WORLD  '

    # swapcase() - Swap case
    print("Hello World".swapcase())  # 'hELLO wORLD'

    # strip() - Remove whitespace from both ends
    print(text.strip())  # 'Hello World'

    # lstrip() - Remove whitespace from left
    print(text.lstrip())  # 'Hello World  '

    # rstrip() - Remove whitespace from right
    print(text.rstrip())  # '  Hello World'

    # find() - Find substring index (returns -1 if not found)
    print(text.find("World"))  # 11

    print(text.find("Python"))  # -1
    # index() - Find substring index (raises ValueError if not found)
    print(text.index("World"))  # 11

    # print(text.index("Python"))  # ValueError
    # rfind() - Find from right
    print(text.rfind("o"))  # 12

    # count() - Count occurrences
    print(text.count("l"))  # 3

    # replace() - Replace substring
    print(text.replace("World", "Python"))  # '  Hello Python  '

    # split() - Split into list
    print(text.split())  # ['Hello', 'World']

    print("1,2,3,4".split(","))  # ['1', '2', '3', '4']
    print("a|b|c".split("|", 1))  # ['a', 'b|c']
    # join() - Join list into string
    print(", ".join(["a", "b", "c"]))  # 'a, b, c'

    print("".join(["H", "e", "l", "l", "o"]))  # 'Hello'
    # startswith() - Check if starts with
    print(text.startswith("  "))  # True

    print(text.startswith("He"))  # False

    # endswith() - Check if ends with
    print(text.endswith("  "))  # True
    print(text.endswith("ld"))  # False

    # isalnum() - Check if alphanumeric
    print("Hello123".isalnum())  # True
    print("Hello 123".isalnum())  # False

    # isalpha() - Check if all letters
    print("Hello".isalpha())  # True
    print("Hello123".isalpha())  # False

    # isdigit() - Check if all digits
    print("123".isdigit())  # True
    print("12.3".isdigit())  # False

    # isspace() - Check if all whitespace
    print("   ".isspace())  # True
    print(" a ".isspace())  # False

    # isupper() - Check if all uppercase
    print("Hello".isupper())  # False

    # islower() - Check if all lowercase
    print("hello".islower())  # True

    # center() - Center string with padding
    print("Hello".center(11, "-"))  # '---Hello---'

    # ljust() - Left justify
    print("Hello".ljust(10, "*"))  # 'Hello*****'

    # rjust() - Right justify
    print("Hello".rjust(10, "*"))  # '*****Hello'

    # zfill() - Pad with zeros
    print("42".zfill(5))  # '00042'
    print("-42".zfill(5))  # '-0042'

    # partition() - Split at first occurrence
    print("a-b-c".partition("-"))  # ('a', '-', 'b-c')

    # rpartition() - Split at last occurrence
    print("a-b-c".rpartition("-"))  # ('a-b', '-', 'c')
    

# complete_stings_method()




# Method Categories:
# Category	Methods
# Case	        || upper(), lower(), capitalize(), title(), swapcase(), casefold()
# --------------||------------------------------------------------------------------------
# Strip	        || strip(), lstrip(), rstrip()
# --------------||------------------------------------------------------------------------
# Search	    || find(), index(), rfind(), rindex(), count(), startswith(), endswith()
# --------------||------------------------------------------------------------------------
# Replace/Split	|| replace(), split(), rsplit(), partition(), rpartition(), join()
# --------------||------------------------------------------------------------------------
# Validation.   || isalnum(), isalpha(), isdigit(), isspace(), isupper(), islower()
# --------------||------------------------------------------------------------------------
# Alignment	    || center(), ljust(), rjust(), zfill()


# ================================
# String Formatting 
# ================================

def string_formatting():
    name = "Alice"
    age = 30
    city = "New York"

    # Basic f-string
    print(f"Hello, {name}! You are {age} years old.")

    # Expressions inside f-strings
    print(f"Next year you'll be {age + 1}.")
    print(f"Your name has {len(name)} characters.")
    print(f"{name.lower()} lives in {city.upper()}.")

    # Formatting numbers
    pi = 3.14159
    print(f"Pi: {pi:.2f}")  # Pi: 3.14
    print(f"Percent: {0.25:.1%}")  # Percent: 25.0%
    print(f"Number: {12345:10d}")  # Number:      12345
    print(f"Hex: {255:#x}")  # Hex: 0xff

    # Multiline f-strings
    message = f"""
    Name: {name}
    Age: {age}
    City: {city}
    """
    print(message)

    # Dictionary unpacking
    person = {"name": "Bob", "age": 25}
    print(f"{person['name']} is {person['age']} years old.")

string_formatting()



def escape_sequence():
    # Newline
    print("Hello\nWorld")
    # Hello
    # World

    # Tab
    print("Hello\tWorld")  # Hello    World

    # Backslash
    print("Hello\\World")  # Hello\World

    # Single quote
    print('Hello\'World')  # Hello'World

    # Double quote
    print("Hello\"World")  # Hello"World

    # Backspace
    print("Hello\bWorld")  # HellWorld

# escape_sequence()


# ====================
# Raw String 
# ====================

def raw_string():
    # Raw strings ignore escape sequences
    path = r"C:\Users\Name\Documents"
    print(path)  # C:\Users\Name\Documents

    # Without raw string (needs escaping)
    path_escaped = "C:\\Users\\Name\\Documents"
    print(path_escaped)  # C:\Users\Name\Documents


# raw_string()


# 8. String Operations

# Concatenation and Repetition
