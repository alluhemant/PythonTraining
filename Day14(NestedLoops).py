# Example:
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # Move to the next line after each row
"""Output:
* * *
* * *
* * *
"""

# Example Print a right-angled triangle pattern using nested loops
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print("----")

"""Example Write a nested loop that prints a 
square pattern of stars (asterisks)."""

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=" ")
    print()

"""Create a nested loop 
to print the multiplication table 
from 1 to 5 (up to 10
times each).
"""
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

"""Write a nested loop to 
print a right-angled triangle of 
numbers in ascending
order
"""
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""Create a nested loop
 that prints a hollow square 
 pattern of stars (asterisks).
"""
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

""" Write a nested loop that prints
 a diamond pattern of stars (asterisks).
"""

n = 5
for i in range(n):
    for j in range(n):
        if (i == n//2 or j == n//2 or i == 1 and j == 1
                or i == 3 and j == 1 or i == 1 and j == 3 or i == 3 and j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end=" ")
    print()