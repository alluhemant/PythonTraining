"""String Indexing
index of first character - 0
index of last character - (length-1)
"""

string = "Hello World!"
first_char = string[0]
print(first_char)

"""Using negative index also we can extract characters
"""
my_string = "Hello World!"
last_char = my_string[-1]
print(last_char)

"""Accessing Individual characters using negative indexing
"""
s = "Genzeon"
last_character = s[-1]
second_last_char = s[-2]
print(last_character)
print(second_last_char)

"""String Slicing"""
string1 = "Hello World!"

substring = string1[0:5]
print(substring)

"""Example: Get the character at index 3."""
string_index3 = string1[3]
print(string_index3)

"""Example: Get a substring 
from index 7 to index 14 (exclusive)"""
substring2 = string[7:]

"""Example: Get a substring from index -9 to -3."""

"""Example: Reverse the sentence using slicing"""

"""Get the length of the sentence using indexing"""
