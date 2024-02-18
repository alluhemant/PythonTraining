"""
Dictionaries are key-value pairs.
These are mutable we can modify.
This is defined using { } and each key-value
pari is separated by colon :
"""

# Creating a dictionary
student = {
    "name": "Hemant",
    "age": "27",
    "department": "mechanical"
}

# Accessing values
# We can access values in dictionary using keys.
# Dictionary keys are unique.

print(student["name"])
print(student["age"])

"""Create an empty dictionary"""
fruits = {}
print(fruits)

""" Create a dictionary to store the age of two people"""
register = {"Hemant": 25, "Kumar": 26}
print(register)

"""Access the value associated with the key "city" from the given
dictionary
"""
dictionary = {"name": "Hemant", "city": "Hubli", "age": 30}
print(dictionary["city"])

"""Create a dictionary to store the contact information of a person.
The person's name is "Bob," and their email is "bob@example.com."""

"""Access the value associated with the key "score" from the given
dictionary."""

""" Create a dictionary to represent a rectangle. The rectangle has a
width of 10 and a height of 5."""

rectangle = input("Enter your dictionary: ")
print(rectangle)

"""Access the value associated with the key "phone" from the given
dictionary. If the key does not exist, return "Not available."""

phone_book = {"name": "hemant", "age": 27}
for i in range(len(phone_book)):
    if phone_book == "phone":
        print("Available")
    else:
        print("not available")


