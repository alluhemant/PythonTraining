"""
For loop is used to iterate over a sequence
(Such as list, tuple, string, or range) and
execute a block of code for each item in sequence

Syntax:
for item in sequence:
    #code block to be executed for each
    item in sequence.
"""

"""Printing numbers from 1 to 5 
using a for loop
"""

for i in range(1, 6):
    print(i)

"""Use a for loop to calculate the sum
 of numbers from 1 to 10"""

sum_of_numbers = 0
for i in range(1, 11):
    sum_of_numbers += i
    i += 1
print("The sum of numbers from 1 to 10 is: ", sum_of_numbers)

"""Write a for loop to print each 
character in the string "Hello"""

String = "Hello"
length = len(String)
for i in range(length):
    print(String[i])
    i += 1

"""Write a for loop to print 
the first 10 even numbers."""
for i in range(20):
    if i % 2 == 0:
        print(i)
    i += 1

"""Create a for loop that doubles each 
number in the sequence: 1, 2, 3, 4, 5."""

for i in range(1, 6):
    print(i * 2)
    i += 1
    