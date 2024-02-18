"""Conditional Statements
if, elif("else if"), else.

Syntax:
if condition1:
   #code block (gets executed if it is true)
elif condition2:
   #code block (gets executed if is false and condition2 is true)
else:
  #code block (gets executed if and else are false)
"""

age = 18
if age >= 18:
    print("Your are eligible to vote!")

"""Using if and else to check conditions"""
age = 15
if age >= 18:
    print("Your are eligible to vote!")
else:
    print("Your are not eligible to vote!")

"""Using if, elif, else statements"""
age = 25
if age < 18:
    print("Minor")
elif 18 <= age <= 65:
    """elif age>=18 and age<=65:"""
    print("Major")
else:
    print("Senior Citizen")

"""Write a program that takes two numbers 
as input and prints the larger number.
"""

"""Write a program that takes a character
 as input and prints "Vowel" if it's a vowel
(a, e, i, o, u), and "Consonant" otherwise."""

Character = str(input("Enter the character to check if it is vowel or constants: "))
vowel = ('a', 'e', 'i', 'o', 'u')
if Character in vowel:
    print("Vowel")
else:
    print("Constants")

"""Write a program that takes a year as 
input and prints "Leap Year" if it's a leap
year, and "Not a Leap Year" otherwise.
"""