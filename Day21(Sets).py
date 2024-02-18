"""
Sets are unordered collection of unique elements
sets are defined by using '{}'or set() constructor.
"""
# Creating a set using '{}'.
my_set = {1, 2, 3, 4, 5}

# Creating a set using set() constructor
another_set = set([1, 2, 3, 4, 5, 6])

# Adding elements to a set

my_set1 = {1, 2, 3}
my_set1.add(4)
print(my_set1)

# Removing elements from set:
my_set2 = {1, 2, 3, 4, 5, 6}
my_set2.remove(3)
print(my_set2)

# Remove an element without raising an error if the element is not present
my_set2.discard(7)

# Pop removes and returns an arbitrary element from the set
popped_element = my_set2.pop()
print(popped_element, my_set2)

"""Creating a set"""
empty_set = ()
print(empty_set)

"""Adding elements to a set"""
Set = {1, 2, 3}
Set.add(4)
print(Set)

"""Removing an element from a set"""
Set.discard(5)
print(Set)

"""Creating a set from a list"""

my_set_list = {input("Enter elements")}
print(my_set_list)
print(type(my_set_list))

"""Adding multiple elements to a set
"""
Set1 = {1, 2, 3}
length = len(Set1)
for i in range(length):
    Set1.add(4)
    Set1.add(5)
print(Set1)

"""Removing elements using discard()"""
Set3 = {10, 20, 30, 40}
Set3.discard(20)
Set3.discard(50)
print(Set3)
