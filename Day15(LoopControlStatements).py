"""Break, Continue, Pass"""

# Example: Using 'break' to stop the loop
# when the value reaches 3

"""The break statement is used to 
terminate a loop prematurely when a certain
condition is met."""

for num in range(1, 9):
    if num == 3:
        break
    print(num)

# Example: Using 'continue'
# to skip printing even numbers
"""statement is used to skip the current 
iteration of a loop and move
to the next iteration."""

for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)

"""pass Statement:
The pass statement is used as a placeholder 
when you don't want to execute
any code inside a loop or a conditional block.
"""

# Example: Using 'pass' to do nothing inside the loop
for num in range(1, 6):
    pass

"""Write a Python program to print all numbers 
from 1 to 10, but stop the loop
immediately when reaching 5 using the break statement."""

for i in range(1, 11):
    if i == 5:
        break
    print(i)

"""Given a list of numbers [1, 2, 3, 4, 5], 
use a for loop to print the elements
one by one. 
However, if the element is 3, skip it using the continue
statement."""

List = [1, 2, 3, 4, 5]
length = len(List)
for i in range(length):
    if List[i] == 3:
        continue
    print(List[i])

"""Write a Python function that takes a 
string as input and checks if it contains
the letter 'o'. 
If it does, print "Found 'o'" and use the break statement to stop
searching
"""

String = "Hello World!"
length_1 = len(String)
for i in range(length_1):
    if String[i].__contains__("o"):
        print("Found o")
        break

"""Given a list of numbers [1, 2, 3, 4, 5], 
use a for loop to double each
element and print the result. However, 
if the element is 4, use the continue
statement to skip it.
"""

list_1 = [1, 2, 3, 4, 5]
for i in range(len(list_1)):
    if list_1[i] != 4:
        var = list_1[i] * 2
        print(var)
        continue

"""Write a Python program to print 
all numbers from 1 to 20 using a while loop.
However, stop the loop when 
reaching 15 using the break statement."""
num = 1
while num <= 20:
    if num != 15:
        print(num)
    else:
        break
    num += 1
