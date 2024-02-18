"""Nested Conditional Statements
"""

x = 10
if x > 0:
    print("X is positive integer")
    if x % 2 == 0:
        print("X is even no")
    else:
        print("X is odd no")
else:
    print("X is not positive number")

"""Nested if-elif-else statements"""
score = 85
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
    if 50 <= score <= 70:
        print("Good Job")
elif score <= 50:
    print("Grade C")
else:
    print("Grade F")

"""Determine the type of a given number 
num : even or odd, and whether it is
positive or negative."""