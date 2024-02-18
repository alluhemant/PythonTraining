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
