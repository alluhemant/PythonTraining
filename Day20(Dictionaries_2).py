# Modifying and Adding key-value pairs

student = {"name": "Hemant", "age": 26, "department": "CS"}

# Modifying values

student["department"] = "Mechanical"

# Adding new values
student["university"] = "VTU"

print(student)

# Dictionary Methods

# get keys and values from dictionary
keys = student.keys()
values = student.values()

print(keys)
print(values)

# Check if key exists in dictionary
if "department" in student:
    print("department:", student["department"])

# Remove a key-value pair from dictionary
removed_Value = student.pop("age")
print("Removed Value: ",removed_Value)

print(student)

"""Given the initial dictionary, modify the value age"""
employee = {"name": "Hemant", "age": 25}
employee["age"] = 27
print(employee)  # {'name': 'Hemant', 'age': 27}

""": Add a new key-value pair 
to the dictionary"""

fruits = {"apple": 5, "banana": 7}
fruits[input("Enter the Key value: ")] = input("Enter the value for key: ")
print(fruits)

"""Given the dictionary remove the Key "sugar"
and its associated value"""

inventory = {"apple": 10, "banana": 15, "sugar": 2}
remove_value = inventory.pop("sugar")
print(inventory)

"""Create a function called add_stock that takes a dictionary stock
and an item item_name (string) as input and adds 1 to the value of the
corresponding key in the dictionary. Return the modified dictionary.
Expected Input: stock = {"apple": 10, "banana": 15} , item_name = "banana"
Expected Output: {"apple": 10, "banana": 16}"""


"""Given the dictionary scores , check if the key "Alice" exists. If it
exists, print the associated value; otherwise, print "Key not found."""

scores = {"Bob": 85, "Charlie": 90, "Alice": 78}
print(scores)
keys = scores.keys()
print(keys)
if "Alice" in keys:
    print("Key Found")
else:
    print("Key not found")

"""Write a function called count_vowels that takes a string text as
input and returns a dictionary containing the count of each vowel (a, e, i, o,
u) in the text. Ignore case sensitivity."""

count_vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
vowels = ("a", "e", "i", "o", "u")
text = "Hello World!"
for i in range(len(text)):
    if text[i] in vowels:
        count_vowels = text[i]
        print(count_vowels)
