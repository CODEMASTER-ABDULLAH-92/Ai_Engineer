# ==========================================
# Python Loops Tutorial
# ==========================================

# ------------------------------------------
# 1. for Loop
# ------------------------------------------

print("For Loop Example:")

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------
# 2. while Loop
# ------------------------------------------

print("\nWhile Loop Example:")

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# ------------------------------------------
# 3. Loop Through a String
# ------------------------------------------

print("\nString Loop Example:")

name = "Abdullah"

for char in name:
    print(char)


# ------------------------------------------
# 4. Loop Through a List
# ------------------------------------------

print("\nList Loop Example:")

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# ------------------------------------------
# 5. break Statement
# ------------------------------------------

print("\nBreak Example:")

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Stops when i becomes 5


# ------------------------------------------
# 6. continue Statement
# ------------------------------------------

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Skips 3


# ------------------------------------------
# 7. pass Statement
# ------------------------------------------

print("\nPass Example:")

for i in range(1, 4):
    pass

print("Loop completed")


# ------------------------------------------
# 8. Nested Loops
# ------------------------------------------

print("\nNested Loop Example:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# ------------------------------------------
# 9. Multiplication Table
# ------------------------------------------

print("\nTable of 5:")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# ------------------------------------------
# 10. Sum of Numbers
# ------------------------------------------

print("\nSum Example:")

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)


# ------------------------------------------
# End of Program
# ------------------------------------------

print("\nProgram Completed!")