"""Variables"""
"""Variables act like a containers, 
we can store our values and we can use them whenever we want them across our 
programs"""

a = "Hemant"
print(a)

a = "Kumar"
print(a)

"""DataTypes"""
"""
1. STRING ("Hemant" , "My Name is Hemant")
      1.1 Capital Letters (A-Z)
      1.2 Small Letters (a-z)
      1.3 Digits (0-9)
      1.4 Special Characters (`! @ # $ % ^ . ? ,)
      1.5 Space
2. INTEGER (EX: 1 , 2 , -9 , 0)
3. FLOAT   (Any Number with decimal points)
4. BOOLEAN (TRUE, FALSE)
"""

"""Integer Data Type"""
my_Integer = 42
print(my_Integer)

"""Float Data Type"""
my_float = 42.0
print(my_float)

"""String Data Type"""
my_string = "Hello World"
print(my_string)

"""Boolean Data Type"""
is_true = True
is_false = False
print(is_true)
print(is_false)

"""Declare two variables a and b , assign integer values to them, and print
their sum."""
a = 5
b = 5
print(a + b)

"""Create a variable name and assign your name to it. Print a greeting message
using your name.
"""
name = "Hemant"
print("Hello "+name)

"""Define a variable pi and assign the value of π (pi) to it. Print the value of
pi ."""
pi = 3.142
print(pi)

"""Define a variable is_raining and ask the user to input either "True" or
"False" (as a string). Convert the input to a boolean and print its type.
"""
is_raining = input("Enter either True or False: ")
print(type(is_raining))
is_raining = bool(is_raining)
print(type(is_raining))

"""Create a string variable sentence containing any sentence of your choice.
Ask the user to input a number, convert it to an integer, and print the
sentence repeated that number of times.
"""
sentence = "Welcome to my world! "
number = int(input("Enter the number: "))
print(sentence * number)

"""Given two variables x and y , perform the following operations and print the
results
Addition of x and y .
Subtraction of y from x .
Multiplication of x and y .
Division of x by y .
x raised to the power of y .
The remainder when x is divided by y .
The floor division of x by y 
"""

"""Define a variable value and assign any numerical value to it. Ask the user to
input a new value. Update the variable value with the new input and print
the updated value."""
Value = 28
new_Value = int(input("Enter your new number: "))
Value = new_Value
print(Value)
