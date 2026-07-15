# =============================
# List?
# =============================
# A list is a mutable, ordered collection of items that can hold elements of different data types.


# ==============================================
# Examples of lists
# ==============================================


empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]  # Can mix types!
nested = [[1, 2], [3, 4], [5, 6]]         # List of lists


# Key Characteristics:

# ✅ Ordered - Items have a defined order (index starting at 0)
# ✅ Mutable - Can be changed after creation (add, remove, modify)
# ✅ Dynamic - Can grow or shrink in size
# ✅ Heterogeneous - Can store different data types
# ✅ Indexable - Access items by index (positive and negative)


# Method 1: Square brackets
list1 = [1, 2, 3]

# Method 2: list() constructor
list2 = list((1, 2, 3))  # From tuple
list3 = list("hello")    # ['h', 'e', 'l', 'l', 'o']

# Method 3: List comprehension
list4 = [x*2 for x in range(5)]  # [0, 2, 4, 6, 8]




# ==================================
# Accessing An Element 
# ==================================


def indexing():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    # Positive indexing (0 to n-1)
    print(fruits[0])   # 'apple'
    print(fruits[2])   # 'cherry'
    print(fruits[4])   # 'elderberry'

    # Negative indexing (-1 to -n)
    print(fruits[-1])  # 'elderberry' (last)
    print(fruits[-2])  # 'date' (second last)
    print(fruits[-5])  # 'apple' (first)

    # Slicing [start:end:step]
    print(fruits[1:4])     # ['banana', 'cherry', 'date']
    print(fruits[:3])      # ['apple', 'banana', 'cherry']
    print(fruits[2:])      # ['cherry', 'date', 'elderberry']
    print(fruits[::2])     # ['apple', 'cherry', 'elderberry']
    print(fruits[::])      # ['apple', 'banana', 'cherry', 'date', 'elderberry'] This will give us the complete list 
    print(fruits[::-1])    # ['elderberry', 'date', 'cherry', 'banana', 'apple']


# indexing()



# =============================================
# Modifying Lists (Adding the Element)
# =============================================



def adding_element():
    fruits = ['apple', 'banana']

    # append() - Add single element at end
    fruits.append('cherry')
    print(fruits)  # ['apple', 'banana', 'cherry']

    # insert() - Add at specific position
    fruits.insert(1, 'blueberry')
    print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']

    # extend() - Add multiple elements
    fruits.extend(['date', 'elderberry'])
    print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

    # Concatenation (+)
    more_fruits = fruits + ['fig', 'grape']
    print(more_fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# adding_element()



# =============================================
# Modifying Lists (Removing Elements)
# =============================================

def remove_elements():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    # Remove the first qurrance of element 
    nums.remove(4)
    print(nums)

    # pop remove the last element from the list 
    nums.pop()
    print(nums)

    nums.pop(1)
    print(nums)

    # delete the element from the specific index or slice 
    del nums[1]
    print(nums)

    # clear the complete list 
    nums.clear()
    print(nums)

# remove_elements()



# =============================================
# Modifying Lists (Updating Elements)
# =============================================

def update_list():
    numbers = [1, 2, 3, 4, 5]

    # Update single element
    numbers[2] = 30
    print(numbers)  # [1, 2, 30, 4, 5]

    # Update slice
    numbers[1:3] = [20, 25]
    print(numbers)  # [1, 20, 25, 4, 5]

    # Replace entire list
    numbers[:] = [10, 20, 30]
    print(numbers)  # [10, 20, 30]


# update_list()


# =============================================
# Common List Methods
# =============================================


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]


# =============================================
# count() - Count occurrences
# =============================================



# Create a sample list
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# count() - Count occurrences
print(nums.count(5))  # 2

# index() - Find first occurrence index
print(nums.index(5))  # 4

# sort() - Sort in-place (ascending)
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# sort() descending
nums.sort(reverse=True)
print(nums)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sorted() - Return new sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(sorted_list)  # [1, 1, 3, 4, 5]
print(original)     # [3, 1, 4, 1, 5] - unchanged

# reverse() - Reverse in-place
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)  # [4, 3, 2, 1]

# copy() - Shallow copy
new_list = nums.copy()
print(new_list)  # [4, 3, 2, 1]

# len() - Get length (built-in function)
print(len(nums))  # 4




# Membership Operators

# Python has two membership operators, in and not in, which test whether a specific value exists inside a sequence or collection. These operations evaluate to boolean values, returning either True or False.

# 1: in
# 1: not in 



def membership_op():
    fruits = ['apple', 'banana', 'cherry']

    # in - Check if element exists
    print('banana' in fruits)    # True
    print('grape' in fruits)     # False

    # not in - Check if element doesn't exist
    print('grape' not in fruits) # True

    # Iteration
    for fruit in fruits:
        print(fruit)


# membership_op()

# Comparison Operators

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)  # True
print(list1 == list3)  # False
print(list1 < list3)   # True (compares element by element)


# =========================
# 2D Arrays 
# =========================

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) #The first is showing row, the second is showing col.
print(matrix[1][2]) #The first is showing row, the second is showing col.

# Accessing the row 
print(matrix[0])


# Iterating through matrix
def iterate_over_matrix():
    for row in matrix:
        for element in row:
            print(element, end=" ")
    
iterate_over_matrix()


# ===============================================
# Copying Lists (Shallow vs Deep):
# ===============================================



# ==========================
# Shallow Copy
# ==========================


# A shallow copy creates a new outer object, but nested (mutable) objects are shared between the original and the copy.

import copy

original = [1, 2, 3, 4]
shallow = copy.copy(original)
shallow[0] = 100
print("Original: ", original)
print("Shallow: ", shallow)

# At here the original is not changed
# But in the case of the nested object it is changed.


original_nested = [[1, 2], [3, 4]]
shallow_nested = copy.copy(original_nested)
shallow_nested[0][0] = 100
print("Original Nested: ", original_nested)
print("Shallow Nested: ", shallow_nested)


# =================
# Deep Copy 
# =================
# In Deep Copy the original values are not changed it remain same 

deep_original = [[1, 2], [3, 4]]

deep = copy.deepcopy(deep_original)

deep[0][0] = 100
deep[0][1] = 200

print("Original Value", deep_original)
print("Deep Copy of Orginal: ", deep)


# deepcopy() creates completely new objects, including all nested objects.

# original  ---> [[1, 2], [3, 4]]

# deep copy ---> [[1, 2], [3, 4]]

# The inner lists are different objects in memory. Therefore, changing the deep copy does not affect the original.



# ==============================
# Unpacking of the List 
# ==============================


# Basic unpacking
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

# Extended unpacking (*)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Swapping variables
a, b = [1, 2]
a, b = b, a
print(a, b)  # 2 1


