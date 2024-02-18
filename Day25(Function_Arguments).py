""" Function Arguments
Position Arguments:
This i basic type of argument. They are matched to
function parameters based on their type order of appearance.
"""


def greet(name, age):
    print(f"Hello, {name}! and {age} years old.")


# Calling the function with positional arguments
greet("Hemant", 27)

"""
KeyWord Arguments:
This are specified with the parameter name followed by the value
, separated by an equal sign.
These arguments allow you to pass the values to the function in any order.
"""


def gree_user(name , age):
    print(f"Hello, {name}! You are {age} years old.")


# Calling the function with keyword arguments in a different order
gree_user(age=27, name="Hemant")


"""
Default Value:
We can provide default values for function parameters.
If a value is not passed for that parameter when the function is called, the default value
will be used.
"""


def greet(name, age=26):
    print(f"Hello, {name}! You are {age} years old.")


# Calling the function without specifying 'age' argument
greet("Hemant")

# Calling the function with 'age' argument
greet("Kumar", 27)


"""
Positional Arguments
Write a function called add that takes two positional arguments a and b , and
returns their sum.
"""


def add(a, b):
    return a + b


result = add(5, 10)
print(result)  # 15


"""
 Keyword Arguments
Write a function called greet that takes two keyword arguments name and age ,
and prints a greeting message with the provided values.
"""


def greet(name, age):
    print(f"Hi, {name} you are {age} years old.")


greet("Alice", age=25)

"""
Default Values
Write a function called multiply that takes two arguments a and b , with b
having a default value of 2. The function should return the product of a and b .
"""


def multiply(a, b=2):
    print(a * b)


multiply(5)  # 10


"""
Mixing Positional and Keyword Arguments
Write a function called print_info that takes three positional arguments name ,
age , and country , and prints the information in a formatted message.
"""


def print_info(name, age, country):
    print(f"Name:{name} Age:{age} Country:{country}")


print_info("NTR", 27, "Bharat")
