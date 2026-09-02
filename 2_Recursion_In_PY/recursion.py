# RECURSION IN PYTHON
# Complete Notes — Fibonacci as the Main Example
#
# ============================================================
# 1. WHAT IS RECURSION?
# ============================================================
#
# Recursion is a programming technique in which a function calls
# itself to solve a smaller version of the same problem.
#
# A recursive function normally has TWO important parts:
#
# 1. BASE CASE
#    The condition that stops the recursion.
#
# 2. RECURSIVE CASE
#    The function calls itself with a smaller/simpler input.
#
# General pattern:
#
# def function(n):
#     if base_condition:
#         return base_answer
#
#     return function(smaller_problem)
#
#
# Example:
#
# def countdown(n):
#     if n == 0:          # BASE CASE
#         return
#
#     print(n)
#     countdown(n - 1)    # RECURSIVE CASE
#
#
# countdown(5)
#
# Output:
# 5
# 4
# 3
# 2
# 1
#
#
# ============================================================
# 2. WHY DO WE NEED A BASE CASE?
# ============================================================
#
# Without a base case, the function keeps calling itself forever.
#
# WRONG:
#
# def test(n):
#     print(n)
#     test(n)
#
# test(5)
#
# Here n never changes, so the function never reaches a stopping
# condition.
#
# Python eventually raises a recursion-related error such as:
#
# RecursionError: maximum recursion depth exceeded
#
# Some coding environments may instead show:
#
# "Step limit exceeded"
#
# The idea is the same: the program is doing too many execution
# steps because the recursion is not terminating.
#
#
# CORRECT:
#
# def test(n):
#     if n == 0:
#         return
#
#     print(n)
#     test(n - 1)
#
#
# test(5)
#
# Execution:
#
# 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> STOP
#
#
# ============================================================
# 3. WHAT DOES return MEAN?
# ============================================================
#
# return sends a value back to the function call that requested it.
#
# Example:
#
# def add(a, b):
#     return a + b
#
# result = add(2, 3)
# print(result)
#
# Output:
# 5
#
# In recursion, return is especially important because one recursive
# call often needs the result produced by another recursive call.
#
#
# ============================================================
# 4. FIBONACCI SEQUENCE
# ============================================================
#
# The Fibonacci sequence begins:
#
# Position:  0   1   2   3   4   5   6   7
# Value:     0   1   1   2   3   5   8  13
#
# The Fibonacci rule is:
#
# F(n) = F(n - 1) + F(n - 2)
#
# But we need starting values:
#
# F(0) = 0
# F(1) = 1
#
# These are called BASE CASES in the recursive implementation.
#
# Then:
#
# F(2) = F(1) + F(0)
#      = 1 + 0
#      = 1
#
# F(3) = F(2) + F(1)
#      = 1 + 1
#      = 2
#
# F(4) = F(3) + F(2)
#      = 2 + 1
#      = 3
#
# F(5) = F(4) + F(3)
#      = 3 + 2
#      = 5
#
#
# ============================================================
# 5. RECURSIVE FIBONACCI FUNCTION
# ============================================================
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(7))
#
# Output:
# 13
#
#
# ============================================================
# 6. WHY DOES n == 1 RETURN 1?
# ============================================================
#
# This is one of the most important points.
#
# Fibonacci is defined with:
#
# F(0) = 0
# F(1) = 1
#
# Therefore:
#
# if n == 0:
#     return 0
#
# if n == 1:
#     return 1
#
# These two values are the starting points from which all later
# Fibonacci values are calculated.
#
# If we returned 0 for n == 1, we would no longer be implementing
# the standard Fibonacci sequence.
#
#
# ============================================================
# 7. WHAT HAPPENS WHEN WE CALL fibonacci(7)?
# ============================================================
#
# We write:
#
# fibonacci(7)
#
# Python enters the function with:
#
# n = 7
#
# Check:
#
# if n == 0:
#
# Is 7 == 0?
# NO.
#
# Next:
#
# if n == 1:
#
# Is 7 == 1?
# NO.
#
# Therefore Python reaches:
#
# return fibonacci(n - 1) + fibonacci(n - 2)
#
# Substitute n = 7:
#
# return fibonacci(6) + fibonacci(5)
#
# VERY IMPORTANT:
#
# This does NOT mean:
#
# 6 + 5
#
# It means:
#
# "Find the Fibonacci value for 6, find the Fibonacci value for 5,
# and then add those TWO RESULTS."
#
#
# ============================================================
# 8. WHICH RECURSIVE CALL HAPPENS FIRST?
# ============================================================
#
# The line:
#
# return fibonacci(n - 1) + fibonacci(n - 2)
#
# contains TWO function calls:
#
# fibonacci(n - 1)
# fibonacci(n - 2)
#
# In normal Python evaluation, the left operand is evaluated before
# the right operand. So the first call is:
#
# fibonacci(n - 1)
#
# For n = 7:
#
# fibonacci(7)
#     |
#     +---- fibonacci(6)  <- first
#     |
#     +---- fibonacci(5)  <- after fibonacci(6) finishes
#
# Python must get the result of fibonacci(6) before it can complete
# the addition with fibonacci(5).
#
#
# ============================================================
# 9. WHAT DOES fibonacci(6) DO?
# ============================================================
#
# fibonacci(6) is neither 0 nor 1.
#
# So:
#
# fibonacci(6)
#     |
#     +---- fibonacci(5)
#     |
#     +---- fibonacci(4)
#
# Again, Python first works on fibonacci(5).
#
# fibonacci(5) becomes:
#
# fibonacci(5)
#     |
#     +---- fibonacci(4)
#     |
#     +---- fibonacci(3)
#
# This continues until a base case is reached.
#
#
# ============================================================
# 10. THE RECURSION TREE FOR fibonacci(7)
# ============================================================
#
#                         F(7)
#                       /     \
#                     F(6)    F(5)
#                    /   \    /   \
#                  F(5) F(4) F(4) F(3)
#                 /  \  / \  / \  / \
#               F4  F3 F3 F2 F3 F2 F2 F1
#              ...
#
# Eventually every branch reaches:
#
# F(1) -> 1
# F(0) -> 0
#
# Then the values are returned upward.
#
#
# ============================================================
# 11. THE "GO DOWN" AND "COME BACK UP" IDEA
# ============================================================
#
# Recursion can be understood in TWO phases.
#
# PHASE 1: GO DOWN
#
# F(7)
#  |
#  v
# F(6)
#  |
#  v
# F(5)
#  |
#  v
# F(4)
#  |
#  v
# F(3)
#  |
#  v
# F(2)
#  |
#  v
# F(1)
#
# At F(1), the base case returns 1.
#
# PHASE 2: COME BACK UP
#
# F(1) -> 1
#   ^
# F(2) -> 1
#   ^
# F(3) -> 2
#   ^
# F(4) -> 3
#   ^
# F(5) -> 5
#   ^
# F(6) -> 8
#   ^
# F(7) -> 13
#
# So the mental model is:
#
#             RECURSION
#                 |
#                 v
#             GO DOWN
#                 |
#                 v
#          REACH BASE CASE
#                 |
#                 v
#          RETURN VALUES UP
#                 |
#                 v
#             FINAL ANSWER
#
#
# ============================================================
# 12. HOW return WORKS IN fibonacci()
# ============================================================
#
# Consider:
#
# return fibonacci(n - 1) + fibonacci(n - 2)
#
# For n = 2:
#
# fibonacci(2)
#     |
#     +---- fibonacci(1) -> 1
#     |
#     +---- fibonacci(0) -> 0
#
# Then:
#
# fibonacci(2)
# = 1 + 0
# = 1
#
# So fibonacci(2) RETURNS 1.
#
# Now consider fibonacci(3):
#
# fibonacci(3)
# = fibonacci(2) + fibonacci(1)
# = 1 + 1
# = 2
#
# So fibonacci(3) RETURNS 2.
#
# Then:
#
# fibonacci(4)
# = fibonacci(3) + fibonacci(2)
# = 2 + 1
# = 3
#
#
# ============================================================
# 13. STEP-BY-STEP CALCULATION OF fibonacci(7)
# ============================================================
#
# The final mathematical calculation is:
#
# F(0) = 0
# F(1) = 1
#
# F(2) = F(1) + F(0)
#      = 1 + 0
#      = 1
#
# F(3) = F(2) + F(1)
#      = 1 + 1
#      = 2
#
# F(4) = F(3) + F(2)
#      = 2 + 1
#      = 3
#
# F(5) = F(4) + F(3)
#      = 3 + 2
#      = 5
#
# F(6) = F(5) + F(4)
#      = 5 + 3
#      = 8
#
# F(7) = F(6) + F(5)
#      = 8 + 5
#      = 13
#
# Therefore:
#
# fibonacci(7) -> 13
#
#
# ============================================================
# 14. A VERY IMPORTANT DIFFERENCE:
#    n - 1 AND n - 2 ARE NOT RESULTS
# ============================================================
#
# When n = 7:
#
# fibonacci(n - 1)
#
# becomes:
#
# fibonacci(6)
#
# and:
#
# fibonacci(n - 2)
#
# becomes:
#
# fibonacci(5)
#
# These are NEW FUNCTION CALLS.
#
# They ask:
#
# "What is F(6)?"
# "What is F(5)?"
#
# The function then recursively finds those answers.
#
# It is NOT simply:
#
# 6 + 5
#
# It is:
#
# F(6) + F(5)
#
# which becomes:
#
# 8 + 5
# = 13
#
#
# ============================================================
# 15. CALL STACK
# ============================================================
#
# Every time a function calls another function, Python keeps track
# of the unfinished function call using the call stack.
#
# Imagine:
#
# fibonacci(7)
#     needs fibonacci(6)
#         needs fibonacci(5)
#             needs fibonacci(4)
#                 needs fibonacci(3)
#                     needs fibonacci(2)
#                         needs fibonacci(1)
#
# At fibonacci(1), Python has reached the base case.
#
# Then calls start finishing in reverse order:
#
# fibonacci(1) -> 1
# fibonacci(2) -> 1
# fibonacci(3) -> 2
# fibonacci(4) -> 3
# fibonacci(5) -> 5
# fibonacci(6) -> 8
# fibonacci(7) -> 13
#
# This "last call finishes first" behavior is associated with a
# STACK (LIFO = Last In, First Out).
#
#
# ============================================================
# 16. WHY ARE THERE TWO RECURSIVE CALLS?
# ============================================================
#
# Fibonacci is defined as:
#
# F(n) = F(n - 1) + F(n - 2)
#
# Therefore the function must ask for TWO previous Fibonacci values.
#
# Example:
#
# F(7) = F(6) + F(5)
#
# F(6) = F(5) + F(4)
#
# F(5) = F(4) + F(3)
#
# This naturally creates a TREE of function calls.
#
#
# ============================================================
# 17. PRINTING THE FIBONACCI SERIES VS FINDING ONE VALUE
# ============================================================
#
# A) FIND THE nth FIBONACCI NUMBER
#
# The function returns ONE value:
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(7))
#
# Output:
# 13
#
#
# B) PRINT THE FIRST n TERMS
#
# We can use the recursive Fibonacci function:
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def print_fibonacci(n):
#     for i in range(n):
#         print(fibonacci(i), end=" ")
#
#
# print_fibonacci(7)
#
# Output:
# 0 1 1 2 3 5 8
#
#
# If the teacher wants the PRINTING itself to be recursive:
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def print_fibonacci(i, n):
#     if i == n:
#         return
#
#     print(fibonacci(i), end=" ")
#     print_fibonacci(i + 1, n)
#
#
# print_fibonacci(0, 7)
#
#
# ============================================================
# 18. FACTORIAL AND FIBONACCI COMPARISON
# ============================================================
#
# Factorial:
#
# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# Fibonacci:
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# Notice:
#
# FACTORIAL asks for ONE smaller problem:
#
# factorial(n - 1)
#
# FIBONACCI asks for TWO smaller problems:
#
# fibonacci(n - 1)
# fibonacci(n - 2)
#
#
# ============================================================
# 19. COMMON MISTAKES IN RECURSION
# ============================================================
#
# MISTAKE 1: NO BASE CASE
#
# def count(n):
#     print(n)
#     count(n - 1)
#
# This never knows when to stop.
#
#
# MISTAKE 2: NOT MOVING TOWARD THE BASE CASE
#
# def count(n):
#     if n == 0:
#         return
#
#     count(n + 1)
#
# Starting at 5 moves:
#
# 5 -> 6 -> 7 -> 8 -> ...
#
# It moves AWAY from 0.
#
#
# MISTAKE 3: WRONG BASE CASE RETURN VALUE
#
# For factorial:
#
# if n == 0:
#     return
#
# This returns None.
#
# Better:
#
# if n == 0:
#     return 1
#
#
# MISTAKE 4: CONFUSING A FUNCTION CALL WITH ITS RESULT
#
# fibonacci(6)
#
# is a FUNCTION CALL.
#
# The result of fibonacci(6) is:
#
# 8
#
# So:
#
# fibonacci(6) + fibonacci(5)
#
# eventually becomes:
#
# 8 + 5
#
#
# ============================================================
# 20. RECURSION WITH PRINT: BEFORE VS AFTER THE CALL
# ============================================================
#
# PRINT BEFORE RECURSION:
#
# def print_numbers(n):
#     if n == 0:
#         return
#
#     print(n)
#     print_numbers(n - 1)
#
# print_numbers(5)
#
# Output:
# 5 4 3 2 1
#
#
# PRINT AFTER RECURSION:
#
# def print_numbers(n):
#     if n == 0:
#         return
#
#     print_numbers(n - 1)
#     print(n)
#
# print_numbers(5)
#
# Output:
# 1 2 3 4 5
#
# Why?
#
# In the second version, recursion goes down first:
#
# 5 -> 4 -> 3 -> 2 -> 1 -> 0
#
# Then print happens while returning:
#
# 1 -> 2 -> 3 -> 4 -> 5
#
#
# ============================================================
# 21. RECURSION VS ITERATION
# ============================================================
#
# ITERATION usually uses loops:
#
# for
# while
#
# RECURSION uses function calls:
#
# function -> function -> function -> ...
#
# Example: sum from 1 to n
#
# ITERATIVE:
#
# def sum_iterative(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
#
#
# RECURSIVE:
#
# def sum_recursive(n):
#     if n == 0:
#         return 0
#
#     return n + sum_recursive(n - 1)
#
#
# Both can calculate:
#
# sum_recursive(5) -> 15
#
#
# ============================================================
# 22. WHEN IS RECURSION USEFUL?
# ============================================================
#
# Recursion is especially useful for problems that naturally have
# smaller versions of themselves or hierarchical structures.
#
# Common examples:
#
# - Fibonacci
# - Factorial
# - Tree traversal
# - Directory traversal
# - Depth-First Search (DFS)
# - Binary search
# - Merge sort
# - Quick sort
# - Backtracking
# - Maze solving
# - N-Queens
# - Generating permutations
# - Generating subsets
#
#
# ============================================================
# 23. THE THREE QUESTIONS TO ASK IN EVERY RECURSION PROBLEM
# ============================================================
#
# QUESTION 1:
# What is the BASE CASE?
#
# Example:
#
# if n == 0:
#     return 0
#
#
# QUESTION 2:
# How do I make the problem SMALLER?
#
# Example:
#
# fibonacci(n - 1)
# fibonacci(n - 2)
#
#
# QUESTION 3:
# How do I COMBINE the smaller answers?
#
# Example:
#
# return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# If you can answer these three questions, you can usually design
# the recursive solution.
#
#
# ============================================================
# 24. FIBONACCI — COMPLETE PROGRAM
# ============================================================
#
# def fibonacci(n):
#     # Base case 1
#     if n == 0:
#         return 0
#
#     # Base case 2
#     if n == 1:
#         return 1
#
#     # Recursive case
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# number = 7
# result = fibonacci(number)
#
# print("Fibonacci number at position", number, "is:", result)
#
# Output:
# Fibonacci number at position 7 is: 13
#
#
# ============================================================
# 25. IMPORTANT PERFORMANCE NOTE
# ============================================================
#
# The simple recursive Fibonacci function is easy to understand,
# but it is NOT efficient for large n.
#
# Why?
#
# The same values are calculated again and again.
#
# For example, F(7) needs F(5) and F(4).
# F(6) also needs F(5) and F(4).
#
# So F(5) and F(4) are recalculated multiple times.
#
# This creates many repeated function calls.
#
# The simple recursive Fibonacci algorithm has exponential time
# growth (commonly described as O(2^n) as a rough bound).
#
# For learning recursion, it is excellent.
# For production code, an iterative or memoized/dynamic-programming
# solution is usually much better.
#
#
# ============================================================
# 26. MEMOIZATION IDEA
# ============================================================
#
# Memoization means storing results that have already been calculated
# so that we do not calculate them again.
#
# Example:
#
# def fibonacci(n, memo=None):
#     if memo is None:
#         memo = {}
#
#     if n in memo:
#         return memo[n]
#
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#     return memo[n]
#
#
# print(fibonacci(50))
#
# The important idea is not to memorize this version yet.
# First understand the basic recursive version completely.
#
#
# ============================================================
# 27. QUICK MENTAL MODEL
# ============================================================
#
# Remember recursion like this:
#
#     FUNCTION
#        |
#        v
#   Is this the base case?
#      /       \
#    YES       NO
#     |         |
#   RETURN     CALL
#   ANSWER    YOURSELF
#               |
#               v
#        SMALLER PROBLEM
#               |
#               v
#          BASE CASE
#               |
#               v
#        RETURN ANSWERS
#
#
# For Fibonacci:
#
# F(7)
#   |
#   +--> F(6)
#   |      |
#   |      +--> F(5)
#   |      +--> F(4)
#   |
#   +--> F(5)
#
# Eventually:
#
# F(1) -> 1
# F(0) -> 0
#
# Then:
#
# F(2) -> 1
# F(3) -> 2
# F(4) -> 3
# F(5) -> 5
# F(6) -> 8
# F(7) -> 13
#
#
# ============================================================
# 28. PRACTICE PROBLEMS
# ============================================================
#
# Practice these in order:
#
# 1. Print numbers from n to 1 recursively.
# 2. Print numbers from 1 to n recursively.
# 3. Print only even numbers from 1 to n recursively.
# 4. Find the sum of the first n natural numbers recursively.
# 5. Find factorial recursively.
# 6. Calculate x^n recursively.
# 7. Find the nth Fibonacci number recursively.
# 8. Print the first n Fibonacci terms.
# 9. Find the sum of digits recursively.
# 10. Count digits recursively.
# 11. Reverse a string recursively.
# 12. Check whether a string is a palindrome recursively.
# 13. Find GCD recursively.
# 14. Find the maximum element of a list recursively.
# 15. Binary search recursively.
#
#


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
