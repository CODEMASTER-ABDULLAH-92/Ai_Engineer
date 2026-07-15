# A tuple is an immutable, ordered collection of items that can hold elements of different data types

empty_tuple = ()
num = (1, 2, 3, 4, 5)
mixed = (1, "mixed", 3.14, True)
nestes = ((1,2), (3,4))
single = (5,)





# =================================
# Key Characteristics:
# =================================


# ✅ Ordered - Items have a defined order (index starting at 0)
# ✅ Immutable - Cannot be changed after creation (no add, remove, modify)
# ✅ Dynamic - Can hold any number of items
# ✅ Heterogeneous - Can store different data types
# ✅ Indexable - Access items by index (positive and negative)
# ✅ Hashable - Can be used as dictionary keys (if all elements are hashable)


#  ===========================================
# Different Ways to Create Tuples:
#  ===========================================

# Method 1: Parentheses

def different_ways_to_create_tuple():
    tuple1 = (1, 2, 3)

    # Method 2: tuple() constructor
    tuple2 = tuple([1, 2, 3])    # From list
    tuple3 = tuple("hello")      # ('h', 'e', 'l', 'l', 'o')
    tuple4 = tuple(range(5))     # (0, 1, 2, 3, 4)

    # Method 3: Without parentheses (tuple packing)
    tuple5 = 1, 2, 3             # (1, 2, 3)

    # Method 4: Single element (must have comma!)
    single = (5,)                # (5,) - This is a tuple
    not_tuple = (5)              # 5 - This is just an integer

    # Method 5: Empty tuple
    empty = ()

    # Method 6: Using comprehension (generator expression)
    tuple6 = tuple(x*2 for x in range(5))  # (0, 2, 4, 6, 8)

# different_ways_to_create_tuple()


# =================================================
# Important: Single Element Tuple
# =================================================

def wrong_way():
    # ❌ WRONG - This is NOT a tuple
    wrong = (5)
    print(type(wrong))  # <class 'int'>

    # ✅ CORRECT - Must include comma
    correct = (5,)
    print(type(correct))  # <class 'tuple'>

    # Also works without parentheses
    also_correct = 5,
    print(type(also_correct))  # <class 'tuple'>

# wrong_way()



# Accessing Elements
# Indexing (Positive and Negative):
# Slicing 

def accessing_and_slicing():
    fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')

# Positive indexing (0 to n-1)
    print(fruits[0])   # 'apple'
    print(fruits[2])   # 'cherry'
    print(fruits[4])   # 'elderberry'

    # Negative indexing (-1 to -n)
    print(fruits[-1])  # 'elderberry' (last)
    print(fruits[-2])  # 'date' (second last)
    print(fruits[-5])  # 'apple' (first)

    # Slicing [start:end:step]
    print(fruits[1:4])     # ('banana', 'cherry', 'date')
    print(fruits[:3])      # ('apple', 'banana', 'cherry')
    print(fruits[2:])      # ('cherry', 'date', 'elderberry')
    print(fruits[::2])     # ('apple', 'cherry', 'elderberry')
    print(fruits[::-1])    # ('elderberry', 'date', 'cherry', 'banana', 'apple')

# accessing_and_slicing()




# =================================
# Tuples are IMMUTABLE
# =================================

# ❌ What You CANNOT Do with Tuples:

# Cannot change element
# Cannot add element
# Cannot remove element
# Cannot delete element

def cannot_do_change_with_tuple():
    fruits = ('apple', 'banana', 'cherry')

    # ❌ Cannot change elements
    fruits[0] = 'orange'  # TypeError: 'tuple' object does not support item assignment

    # ❌ Cannot add elements
    fruits.append('date')   # AttributeError: 'tuple' object has no attribute 'append'

    # ❌ Cannot remove elements
    fruits.remove('banana')  # AttributeError: 'tuple' object has no attribute 'remove'

    # ❌ Cannot delete elements
    del fruits[1]  # TypeError: 'tuple' object doesn't support item deletion

# cannot_do_change_with_tuple()



# ===========================================
# ✅ What You CAN Do with Tuples:
# ===========================================

# Reassign the tuple
# Concate the tuple
# Slice the tuple
# repeat the tuple


def can_we_do_with_tuple():
    fruits = ('apple', 'banana', 'cherry')

    # ✅ Reassign the entire tuple
    fruits = ('orange', 'grape', 'mango')  # This is allowed!

    # ✅ Concatenate (creates new tuple)
    new_fruits = fruits + ('date', 'elderberry')
    print(new_fruits)  # ('orange', 'grape', 'mango', 'date', 'elderberry')

    # ✅ Multiply (repetition)
    repeated = ('hi',) * 3  # ('hi', 'hi', 'hi')

    # ✅ Slice (creates new tuple)
    sliced = fruits[1:3]  # ('grape', 'mango')

# can_we_do_with_tuple()




# 5. Tuple Methods
# Tuples have only two methods (since they're immutable):

def tuple_method():
    # Create a sample tuple
    nums = (3, 1, 4, 1, 5, 9, 2, 6, 5)
    
    # count() - Count occurrences
    print(nums.count(5))  # 2
    print(nums.count(1))  # 2
    
    # index() - Find first occurrence index
    print(nums.index(5))  # 4
    print(nums.index(1))  # 1
    
    # index() with start and end
    print(nums.index(5, 5))  # 8 (search from index 5 onwards)
    
    # len() - Get length (built-in function)
    print(len(nums))  # 9
    
    # in / not in - Membership
    print(5 in nums)    # True
    print(10 in nums)   # False
    print(10 not in nums)  # True

# tuple_method()



# Tuple Iteration

def tuple_Iteration():
    fruits = ('apple', 'banana', 'cherry', 'mango')

    for i in fruits:
        print(i)
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")
# tuple_Iteration()


#============================== 
# Comparison Operators
#==============================

def comparison():
    
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    tuple3 = (1, 2, 4)
    
    print(tuple1 == tuple2)  # True
    print(tuple1 == tuple3)  # False
    print(tuple1 < tuple3)   # True (compares element by element)

# comparison()


# Tuple Unpacking

def tuple_Unpacking():
    # Unpacking tuple into variables
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    print(x, y, z)  # 10 20 30

    # Swapping variables using tuples
    a, b = 5, 10
    a, b = b, a  # Swap
    print(a, b)  # 10 5

    # Multiple assignment
    name, age, city = ("Alice", 25, "New York")
    print(name, age, city)  # Alice 25 New York

tuple_Unpacking()



def extended_unpacking():
    first, *middle, last = (1,2,3,4,5,6)
    print(first)
    print(middle)
    print(last)

    *beginer, last = (1,2,3,4)
    print(beginer)
    print(last)

# extended_unpacking()



def get_user_info():
    name = "Muhammad Abdullah"
    age = 23
    city = "New York City"

    return name, age, city

name, age, city = get_user_info()
print(name)
print(age)
print(city)


# Use Tuple When:
# ✅ Data should not change (immutable)
# ✅ You want to use as dictionary key or set element
# ✅ Performance is important (memory and speed)
# ✅ Data is heterogeneous (different types)
# ✅ Return multiple values from a function
# ✅ Represent fixed collections (e.g., coordinates, RGB values)
# ✅ You want to protect data from accidental modification



# Use List When:
# ✅ Data needs to change (mutable)
# ✅ You need to add/remove elements frequently
# ✅ Data is homogeneous (same type)
# ✅ You need to sort or reverse the data
# ✅ You're not sure about the final size
# ✅ You need methods like append(), extend(), pop()

