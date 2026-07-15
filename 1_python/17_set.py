# ===========================
# Set 
# ===========================

# A set is a mutable, unordered collection of unique, hashable elements. Sets are optimized for fast membership testing and mathematical set operations.


empty_set = set()  # Note: {} is empty dict, not set
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}  # Can mix types!
frozen = frozenset([1, 2, 3])      # Immutable set

# # Set from list (removes duplicates)
unique_numbers = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Key Characteristics:
# ✅ Unique Elements - No duplicates allowed
# ✅ Mutable - Can add/remove elements
# ✅ Unordered - No index, no order guarantee
# ✅ Fast Membership - O(1) average time complexity for in checks
# ✅ Mathematical Operations - Union, intersection, difference, etc.


# ==========================
# Creating the Set 
# ==========================

# Method 1: Curly braces
set1 = {1, 2, 3, 4, 5}

# Method 2: set() constructor
set2 = set([1, 2, 3, 4])           # From list
set3 = set((1, 2, 3, 4))           # From tuple
set4 = set("hello")                # {'h', 'e', 'l', 'o'}
set5 = set(range(5))               # {0, 1, 2, 3, 4}

# Method 3: Set comprehension
set6 = {x**2 for x in range(5)}    # {0, 1, 4, 9, 16}
set7 = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# Method 4: Empty set (must use set())
empty_set = set()
# empty_set = {}  # This is a dictionary, not a set!

# Method 5: Using set() with string
set8 = set("apple")  # {'a', 'e', 'p', 'l'}

# Method 6: From other iterable
set9 = set(range(10, 20, 2))  # {10, 12, 14, 16, 18}


# =======================================
# Accessing Elements
# Sets are NOT Indexable because this is unordered: (So we can not accessing the elements )
# =======================================

my_set = {1, 2, 3, 4, 5}

# ❌ Cannot access by index
# print(my_set[0])  # TypeError: 'set' object is not subscriptable


# ===========================
# MemberShip Operator 
# ===========================

def memberShip():
    my_set = {1,2,3,4}
    print(3 in my_set)
    print(12 in my_set)
    print(10 not in my_set)
    
# memberShip()


def iteration():
    my_set = {1,2,3,4,4}
    
    for element in my_set:
        print(element)
    
    # With index (enumerate works but order is arbitrary)
    
    for key, val in enumerate(my_set):
        print(f"{key}: {val}")
    
    # Sorted Iteration:
    
    for element in sorted(my_set):
        print(element)
# iteration()






# ✅ Get a specific element (if needed)
# Since sets are unordered, you can't get "first" element
# But you can pop() which removes and returns an arbitrary element
element = my_set.pop()  # Removes and returns arbitrary element
print(element)
my_set.add(element)  # Add it back if needed





# =====================
# Modifying Sets
# =====================

def modifying_set():
    my_set = {1,2,3,4}
    my_set.add(5)
    
    my_set.add(5)
    
    my_set.update([5,6,7,8])
    
    my_set.update('abc')
    
    my_set |= {10, 12,14}
    
    print(my_set)

# modifying_set()


set_my = {1,2,3,4}
set_my |= {4,5,6,7}

print(set_my)


def removing_element():
    my_set = {1, 2, 3, 4, 5, 6, 7}

    # remove() - Remove specific element (raises KeyError if missing)
    my_set.remove(5)
    print(my_set)  # {1, 2, 3, 4, 6, 7}
    # my_set.remove(10)  # KeyError: 10

    # discard() - Remove element if exists (no error if missing)
    my_set.discard(6)
    print(my_set)  # {1, 2, 3, 4, 7}
    my_set.discard(10)  # No error

    # pop() - Remove and return arbitrary element
    popped = my_set.pop()
    print(f"Removed: {popped}")
    print(my_set)

    # clear() - Remove all elements
    my_set.clear()
    print(my_set)  # set()

    # del - Delete entire set
    # del my_set
    
# removing_element()




# ===============================
# set Common Methods 
# ===============================

def set_common_method():
    # Create sets for demonstration
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # add() - Add element
    set1.add(6)
    print(set1)  # {1, 2, 3, 4, 5, 6}

    # remove() - Remove element (KeyError if missing)
    set1.remove(6)
    print(set1)  # {1, 2, 3, 4, 5}

    # discard() - Remove if exists (no error)
    set1.discard(10)  # No error

    # pop() - Remove arbitrary element
    popped = set1.pop()
    print(f"Popped: {popped}")

    # clear() - Remove all
    set1.clear()
    print(set1)  # set()

    # copy() - Shallow copy
    original = {1, 2, 3}
    copy_set = original.copy()
    print(copy_set)  # {1, 2, 3}

    # union() - All elements from both sets (|)
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union = set1.union(set2)
    print(union)  # {1, 2, 3, 4, 5}
    print(set1 | set2)  # {1, 2, 3, 4, 5}

    # intersection() - Common elements (&)
    intersection = set1.intersection(set2)
    print(intersection)  # {3}
    print(set1 & set2)  # {3}

    # difference() - Elements in first but not second (-)
    difference = set1.difference(set2)
    print(difference)  # {1, 2}
    print(set1 - set2)  # {1, 2}

    # symmetric_difference() - Elements in either but not both (^)
    sym_diff = set1.symmetric_difference(set2)
    print(sym_diff)  # {1, 2, 4, 5}
    print(set1 ^ set2)  # {1, 2, 4, 5}

# set_common_method()




# Set Operations Methods with Update:


def set_operations_with_update():
    
    set1 = {1,2,3}
    set2 = {3,4,5}
    
    
    #=====================================================
    # set3 = set1 |= set2 Here an Error check it 
    #=====================================================
    
    
    set1.update(set2)
    
    
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    # update() - Add elements from another set (|=)
    set1.update(set2)
    print(set1)  # {1, 2, 3, 4, 5}

    # intersection_update() - Keep only common elements (&=)
    set1 = {1, 2, 3}
    set1.intersection_update(set2)
    print(set1)  # {3}

    # difference_update() - Remove elements in other set (-=)
    set1 = {1, 2, 3}
    set1.difference_update(set2)
    print(set1)  # {1, 2}

    # symmetric_difference_update() - Keep elements in either but not both (^=)
    set1 = {1, 2, 3}
    set1.symmetric_difference_update(set2)
    print(set1)  # {1, 2, 4, 5}

    
# set_operations_with_update()


