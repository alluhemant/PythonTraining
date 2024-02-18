"""Python Lamda
A lamda is a small anonymous function.

A lamda can take any no of arguments, but can only
have one expression.

SYNTAX:

lamda arguments : expression
"""
# Example
x = lambda a: a + 10
print(x(5))

# Can take any no of arguments
y = lambda a, b: a * b
print(y(2, 2))


def myfun(n):
    return lambda a: a * n


doubler = myfun(5)
print(doubler(2))

"""
Python Arrays
Python does not have a built in's for Arrays,
Python lists can be used instead.

Note: 
This you how to use LISTS as ARRAYS, however, 
to work with arrays in Python you will have to import a library, 
like the NumPy library.
"""

cars = ["Hemant", "kumar", "Genzeon"]

single = cars[0]
# modify
cars[0] = "Python"

"""
The length of an array is always 
one more than the highest array index.
"""

"""
Python Classes and Objects
"""

# Create Class:


class MyClass:
    x = 5


print(MyClass)  # <class '__main__.MyClass'>


# Create Object
#  named p1, and print the value of x:

p1 = MyClass()
print(p1.x)


"""
The __init__() Function
It is a built in function.

All classes have this function, which always executed when the
class is being initiated.
"""

# Example


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Hemant", 27)
print(person1.name)
print(person1.age)

# The __init__ function is called automatically every time the class
# is being used to create a new object

"""
The __str()__ function
This function controls what should be returned when the class object is represented as a string.

If the function is not set, the string representation of the object is returned:
"""

# Example The string representation without __str__() function:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Kumar", 28)
print(p1)


# Example The string representation with __str__() function:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"


p1 = Person("Kumar", 28)
print(p1)

"""
Object Methods
Object can also contain methods, Methods in Objects are functions that belong
to the the Object.
"""

# Insert a function that prints a greeting, and executed it on the p1 object:

class Person:
    def __init__(self, company, age):
        self.company = company
        self.age = age

    def myfunc(self):
        print(f"I am working in : {self.company}")


p1 = Person("Genzeon", 28)
p1.myfunc()


"""
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
"""


class Person:
    pass

