set1 = {1, 2, 3, 4, 5}


def find(x):
    for i in range(len(set1)):
        if x in set1:
            return f"Element", x, " is present in set"
        i += 1
    else:
        return f"Element", x, " is not present in set"


result = find(int(input("Enter the element to find in set: ")))
print(result)


# Remove duplicates elements from set
Set_Duplicates = {1, 2, 1, 3, 4, 3}
print(set(Set_Duplicates))  # set() method removes the duplicates.

# Check if one set is subset of another

set3 = {1, 2, 3, 4, 5}
set4 = {2, 3, 1, 6, 4}
set5 = {1, 2, 3, 4, 5}
print(set4.issubset(set3))  # not subset
print(set5.issubset(set3))  # is subset

"""Set Operation"""
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# union of two sets
union_set = set1.union(set2)
print(union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)

# Symmetric difference  (elements in either set, but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# Membership test
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)
print(6 in my_set)
