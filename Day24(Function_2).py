# Default parameters:
def greet_user(name="Guest"):
    print(f"Hello, {name}!")


greet_user()  # Hello, Guest!
greet_user("Hemant")  # Hello, Hemant!


# Calling functions inside functions:
def greet(name):
    return f"hello, {name}!"


def greet_and_emphasize(name):
    greeting = greet(name)
    return greeting.upper() + "!!!"


result = greet_and_emphasize("Hemant")
print(result)  # HELLO, HEMANT!!!!

# Scope of variable:
"""
If we declare variables as Global we can use them across the project
If we declare variables inside a function then that variable can be used
only inside that particular function.
"""

global_variable = "Global"


def function_with_local_variable():
    local_variable = "Local"
    print(global_variable)
    print(local_variable)


function_with_local_variable()
print(global_variable)
# print(local_variable)


"""
Simple function with a default parameter
Write a function called greet_user that takes an optional name parameter with a
default value of "Guest". The function should return a greeting message with the
provided name or "Guest" if no name is provided.
"""


def greet_user1(name="Guest"):
    print(f"Hello, {name}!")


greet_user1()
greet_user1("hemant")

"""
: Function with multiple parameters
Write a function called calculate_sum that takes three parameters a , b , and c ,
and returns the sum of the three numbers

"""


def calculate_sum(a, b, c):
    return a + b + c


result = calculate_sum(5, 10, 15)
print(result)  # 30

"""
Function calling another function
Write a function called square that takes a number x as input and returns the
square of that number. Then, write a function called square_and_double that takes
a number x , calls the square function, and returns twice the square value.

"""


def square(x):
    return x * x


def square_and_double(x):
    number = square(x)
    return number + number


result = square_and_double(5)
print(result)  # 50

"""
Nested functions and variable scopes
Write a function called outer_function that has a local variable outer_variable
with the value "I'm outer". Inside the outer_function , define another function
called inner_function that has a local variable inner_variable with the value "I'm
inner". The inner_function should print both the outer_variable and
inner_variable . Then, call the outer_function and print the outer_variable outside
the function.

"""


def outer_function():
    outer_variable = "I'm outer"
    return outer_variable


def inner_function():
    inner_variable = "I'm inner"
    output = outer_function()
    print(inner_variable)
    print(output)


inner_function()
print(outer_function())

"""
 Function returning multiple values
 Write a function called divide_and_remainder that takes two numbers a and b as
input and returns their division result and remainder.
"""


def divide_and_remainder(a, b):
    division = a % b
    remainder = a // b
    return division, remainder


result = divide_and_remainder(15, 4)
print(result)

"""
Recursive function
Write a recursive function called factorial that takes a positive integer n as
input and returns its factorial.
"""

fact1 = 1


def factorial(n):
    global fact1
    for i in range(1, n + 1):
        fact1 = fact1 * i
        i += 1
    return f"The factorial of,{n}: {fact1}"


result_fact = factorial(5)
print(result_fact)  # 120
