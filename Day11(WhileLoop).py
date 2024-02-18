"""Syntax
while condition:
    #code block to be executed while the condition is true
"""

"""Printing numbers from 1 to 5 
using a while loo"""

num = 1
while num <= 5:
    print(num)
    num += 1

"""Finding the sum of numbers from 1 to 10 
using a while loop"""

num = 1
sum_of_no = 0

while num <= 10:
    sum_of_no += num
    num += 1
print("Sum of no's from 1 to 10: ", sum_of_no)

"""Write a while loop that prints 
numbers from 1 to 10."""

num = 1
while num <= 10:
    print(num)
    num += 1

"""Create a while loop that calculates
the sum of numbers from 1 to n,
where n is the input"""

num = 1
sum_of_nos = 0
n = int(input("Enter the number: "))
while num <= n:
    sum_of_nos += num
    num += 1
print("Sum of no's using generic way: ", sum_of_nos)

"""Write a while loop that
 prints even numbers from 2 to 10."""

num = 1
n1 = int(input("Enter the no: "))

while num <= n:
    if num % 2 == 0:
        print("Even no: ", num)
    else:
        print("Odd no: ", num)
    num += 1


