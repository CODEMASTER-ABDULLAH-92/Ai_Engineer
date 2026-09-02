# Recursion is a when a function calls itself.
# Recursion is need a base case to stop the recursion, otherwise it will go into infinite loop.

# Recursion has two main components:
# 1. Base Case: The condition under which the recursion stops.
# 2. Recursive Case: The part of the function where it calls itself.

# Lets take an example:

def count_down(n):
    
    # Base Case:
    if n == 0:
        print("End: ")
        return
    count_down(n - 1)
    print(n)

count_down(5)



def print_numbers(n):

    if n == 0:
        return
    
    print("Before: ", n)
    print_numbers(n - 1)

    print("After: ",n)


print_numbers(5)



def calculate_sum(n):
    
    total = 0
    
    for i in range(1, n + 1):
        total += i
    
    return total

sum_num = calculate_sum(5)
print(sum_num)
