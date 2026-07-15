# ========================================================
# Pythonic Thinking: Iterators and Generators 
# ========================================================


# Non-Pythonic (C-style loop)

numbers = [1, 2, 3, 4, 5]
squares = []
for i in range(len(numbers)):
    squares.append(numbers[i] ** 2)

# Pythonic (List comprehension)
squares = [x ** 2 for x in numbers]




# An iterable is a collection of data. An iterator is an object that remembers the current position and returns one item at a time. A for loop automatically converts an iterable into an iterator by calling iter(), then repeatedly calls next() until StopIteration is raised.


# Easy way to remember

# - Iterable = A collection you can loop over (like a list, tuple, string).
# - Iterator = An object that keeps track of where you are and gives the next item each time you ask.
# - iter(iterable) → Creates an iterator.
# - next(iterator) → Gets the next item.
# - When no items remain → StopIteration is raised.



class countDown:
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        result = self.current
        self.current -= 1
        return result

for num in countDown(5):
    print(num) 


text = "Python"
it = iter(text)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))




# Pythonic for loop
for item in [1, 2, 3]:
    print(item)

# What happens behind the scenes:
iterable = [1, 2, 3]
iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break


# ============================
# Generators in Python
# ============================

# A generator is a special type of function that produces values one at a time instead of returning all values at once. It uses the yield keyword instead of return.

# Unlike a normal function, a generator remembers its state between calls and resumes execution from where it stopped.


# Normal Function (return)

# A normal function returns a value and then terminates.

def numbers():
    return 1
    return 2  # Never executes

print(numbers())

# Once return executes, the function ends.


# Generator Function (yield)

# A generator yields one value at a time.

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()
print("Yields: ",next(gen))
print("Yields: ",next(gen))
print("Yields: ",next(gen))

#=======================
# How yield Works
#=======================

# When Python reaches yield:

# 1. It returns the current value.
# 2. It pauses the function.
# 3. It saves all local variables.
# 4. On the next next() call, it resumes from where it paused.



def demo():
    print("Start: ")
    yield 10
    
    print("Middle")
    yield 20
    
    print("End...")
    yield 30

for num in demo():
    print(num)
    
    
# ===================================
# Why do we use generators?
# ===================================

# The main purpose of a generator is to generate data only when it is needed (lazy evaluation) instead of creating everything at once.

# Main Purpose
# Generators are used to:

# 1. Save memory.
# 2. Handle very large datasets.
# 3. Process data one item at a time.

