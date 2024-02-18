"""Using functions we can create a reusable code

Creating a function

We use "def" keyword followed by a function name, a ()
and a colon :.
The code block inside the function is indented
and contains instructions that function will be executed when called.
"""


def greeting():
    print("Hello")


# Calling the function
greeting()

"""Function Parameters
We can define parameters inside the () to pass data into the function.
This '()' act as a place holder for actual values
that you provide when calling function 
"""


def greet(name):
    print(f"Hello", name)


# Calling the function with an argument
greet("Hemant")

""" Return Statement
Functions can return values using the 
"return" keyword. 
When a function returns a value, you can capture and use it elsewhere in your code 
"""


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(result)

"""
Simple function without parameters
"""


def greeting():
    print("hello")


greeting()

"""Function with one parameter"""


def greet_user(name):
    print(f"Hello", name)


greet_user(input("Enter your name: "))

""" Function with two parameters and 
mathematical operation"""


def add_numbers(a, b):
    return a * b


result = add_numbers(5, 10)
print(result)

"""Function with a conditional statement
"""


def even_odd(number):
    if number % 2 == 0:
        return "even no"
    else:
        return "odd no"


results = even_odd(7)
print(results)

"""Function with default parameter value"""
"""Write a function called greet_user that takes an optional name parameter with a
default value of "Guest". The function should return a greeting message with the
provided name or "Guest" if no name is provided"""


def greetings(name):
    if name == "":
        print("Hello Guest!")
    else:
        print(f"Hello", name)


greetings(input("Enter the name: "))

""" Function with a variable number of arguments (variadic
function)
Write a function called sum_numbers that takes a variable number of arguments
and returns the sum of all the arguments.
"""


def sum_numbers(a, b, c, d, e):
    return a + b + c + d + e


result = sum_numbers(2, 4, 6, 8, 10, )
print(result)


"""Nested Functions
Write a function called square that takes a number x as input and returns the
square of that number using a nested function called multiply to perform the
calculation."""


def square(x):
    return f"The square is: ", {x}


def multiply(x):
    number = square(x)
    return number


result = multiply(5)
print(result)
