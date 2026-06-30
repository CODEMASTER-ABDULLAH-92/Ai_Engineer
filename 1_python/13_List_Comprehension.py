# ===============================
# List comprehensions
# ===============================

# List comprehensions provide a concise way to create lists in Python. They're often more readable and faster than using loops with append()


# ===============================
# Full Syntax 
# ===============================

# [expression for item in iterable if condition]


# Traditional loop
squares = []
for x in range(5):
    squares.append(x * x)
# print(squares)  # [0, 1, 4, 9, 16]

# List comprehension (same result)
squares = [x * x for x in range(5)]
# print(squares)  # [0, 1, 4, 9, 16]



evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

square_even = [x * x for x in range(10) if x % 2 == 0]
print(square_even)
