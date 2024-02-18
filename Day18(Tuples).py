"""Tuples are immutable--->
If we create once we cant add or remove elements
We close elements in () for tuple
"""

# Example: Creating a tuple
fruits = ("apple", "banana", "orange")
numbers = (1, 2, 3.14, 2.40)

# Accessing elements:

print(fruits[0])  # "apple"
print(fruits[2])  # "orange"

"""Tuple packing and un-packing"""
person = ("Hemant", 30, "Hubli")
name, age, city = person

print(name)
print(age)
print(city)

"""Tuple Functions"""
number = (5, 2, 8, 1, 7)

# length of the tuple
length = len(number)
print(length)

# Maximum and Min elements in tuple
maximum = max(tuple)
minimum = min(tuple)
print(maximum, minimum)

# We can concat and repeat tuples to

"""Create a tuple containing three elements:
 'apple', 5, and True."""

tuples = ("apple", 5, True)
print(tuples)

"""Access the second element from the given tuple: 
('cat', 'dog', 'bird', 'fish')."""

tuples_1 = ('cat', 'dog', 'bird', 'fish')
print(tuples_1[1])

"""Concatenate two tuples: (1, 2, 3) and ('a', 'b', 'c').
"""

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
print(tuple1 + tuple2)

"""Find the length of the tuple: """
"""Check if the element 25 exists in the tuple:"""
"""Create a new tuple with elements from the given tuple (3, 6, 9) repeated 3
times"""
"""Perform packing and unpacking on a tuple containing the names of three
fruits: 'apple', 'banana', and 'orange'. Use unpacking to assign each fruit to
three variables: fruit1, fruit2, and fruit3."""

