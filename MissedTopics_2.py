"""
Python Inheritance:

Inheritance allows us to define a class that inherits all the
methods and properties from another class.

Parent Class:
Is the class being inherited from also called base class.

Child Class:
Is the class that inherits from another class, also called derived class
"""


# Creating a Parent class:


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


# Using the person class to create an object, and then execute
# printname method


x = Person("Hemant", "Kumar")
x.printname()

# Create a child class:


class Student(Person):
    pass


x = Student("Kumar", "Hemant")
x.printname()

# Adding the __init__() func to child class

# class Student(Person):
#    def __init__(self, fname, lname):
                # add properties etc.

# When you add the __init__() function, the child class will no longer
# inherit the parent's __init__() function

"""
Note: The child's __init__() function overrides
the inheritance of the parent's __init__() function.
"""

# To keep inheritance of the parent's
# __init__ func add a call to parent's __init__func:


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# ------------- OR --------------


# class Student(Person):
#    def __init__(self, fname, lname):
#        super.__init__(fname, lname)

# Adding properties


# class Student(self, fname, lname):
#    def __init__(self, fname, lname):
#        super().__init__(fname, lname)
#        self.graduation_year = 2018


# Add a year parameter, and pass the correct year when creating objects:

"""
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

"""


"""Python Iterators"""
"""
Iterator is an object that contains countable no of values
Where on iterator object can be iterated upon, We can traverse through all the values.
It consist of the methods __iter__() and __next__(). 
"""

"""Iterator vs iterable
Lists, tuples, sets , dictionaries and Strings are 
iterable objects.

All these objects have a iter() method which is used to get an iterator:
"""

my_tuple = ("apple", "banana", "grapes")
my_it = iter(my_tuple)

print(next(my_it))
print(next(my_it))
print(next(my_it))


myStr = "banana"
my_str = iter(myStr)

print(next(my_str))  # b
print(next(my_str))  # a


# We can also use a for loop to iterate through an iterable object:
# for x in my_tuple:
#      print(x)


# Creating an Iterator

class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = Numbers()
my_iter1 = iter(my_class)

print(next(my_iter1))
print(next(my_iter1))


# StopIteration
# We can use to stop iteration from going on forever

class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = Numbers()
my_iter1 = iter(my_class)

for x in my_iter1:
    print(x)


"""Class Polymorphism"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x)


"""Inheritance Class Polymorphism"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail")


class Plain(Vehicle):
    def move(self):
        print("Fly")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()