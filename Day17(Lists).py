"""Lists are mutable(We can modify)"""

"""Creating Lists"""
numbers = [1, 2, 3, 4, 5]

"""Creating a List of strings"""
string = ["apple", "banana", "orange"]

"""Creating a mixed-type list"""
mixed_list = [1, "apple", True, 3.14]

"""Accessing Elements"""
fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[2])

"""Modifying Elements"""
fruits[1] = "grape"
print(fruits)

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
result = list1 + list2
print(result)

# Repeating
repeated_list = list1 * 3
print(repeated_list)

# List Methods
fruits = ["apple", "banana", "orange", "mango"]

# Adding new elements into list
print(fruits)

# Removing Elements
fruits.remove("orange")
print(fruits)

# Sorting Elements
fruits.sort()
print(fruits)


"""Write a Python program 
that takes a list of numbers [1, 2, 3, 4, 5] and prints
each number on a new line."""

list_of_numbers = [1, 2, 3, 4, 5]
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i])

"""Given a list of strings ["apple", "banana", "orange"], 
concatenate all the
strings together with a space in between 
and print the result."""

fruits = ["apple", "banana", "orange"]
strings = 0
for i in range(len(fruits)):
    print(fruits[i], end=" ")
    print()

"""Write a Python function 
that takes a list of numbers as input and returns the
sum of all the numbers."""

list_of_nos = [1, 2, 3, 4, 5]
sum_of_nos = 0
for i in list_of_nos:
    sum_of_nos += i
    i += 1
print(sum_of_nos)

"""Given a list of numbers 
[10, 20, 30, 40, 50], find the maximum number using
the max() 
function and print the result."""

numbers = [10, 20, 30, 40, 50]
maximum = max(numbers)
print(maximum)

"""Write a Python program that takes a list of names ["Alice", "Bob", "Charlie"]
and checks if a given name (e.g., "Alice") is 
present in the list. Print "Name
found" if the name is in the list; otherwise, print "Name not found"""

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    if names[i] == "Alice":
        print("Name Found")
    else:
        print("Name not found")

