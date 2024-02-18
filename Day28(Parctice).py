"""
Create a variable name and assign your name to it. Print a greeting message
using the variable.
"""

name = "Hemant"
print(name)  # Hemant


"""
Convert the string "42" to an integer and assign it to a variable num . Print
the value and type of num .
"""

String = "42"
num = int(String)
print(num)  # 42
print(type(num))  # <class 'int'>

"""
Define a tuple with three elements: "cat" , "dog" , and "rabbit" . Print the
third element
"""

tuple = ("cat", "dog", "rabbit")
for i in range(len(tuple)):
    if tuple[i] == "rabbit":
        print(tuple[i])


"""
Swap the values of two variables, a and b , without using a temporary
variable.
"""

a = 5
b = 10
temp = a
a = b
b = temp
print(f"a: {a}")
print(f"b: {b}")


"""
Write a program that takes your age as input and prints a message: "You are
[age] years old."
"""


def print_info(age):
    print(f"You are {age} years old.")


print_info(int(input("Enter your age: ")))


"""
Calculate the product of two numbers entered by the user and print the
result.
"""


def product(a, b):
    return f"The product of a={a}, b={b} is: {a * b}"


result = product(int(input("Enter the value of a: ")), int(input("Enter the value of b: ")))
print(result)

"""
Format the variables item = "book" and price = 25.99 into a sentence
"""

item = "book"
price = 25.99

print(f"The cost of the {item} is {price}")


"""
Write a function that takes an integer as input and returns "Positive" ,
"Negative" , or "Zero" .
"""


def find(num):
    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positive")
    else:
        print("Zero")


find(int(input("Enter the no to find +ve, -ve, or zero: ")))


"""
Create a program that checks if a user-input number is even or odd.
"""


def even_odd(X):
    if X % 2 == 0:
        print(f"The no:{X} is even no.")
    else:
        print(f"The no:{X} is odd no.")


even_odd(int(input("Enter the no to check even or odd: ")))


"""
Write a program that determines if a year entered by the user is a leap year.
"""


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year")


leap_year(int(input("Enter the year to find leap year or not: ")))


"""
Print the numbers from 1 to 5 using a for loop.
"""

for i in range(5):
    print(i)

"""
Write a while loop that calculates the sum of numbers from 1 to 20.
"""

num =1
Sum_of_nos = 0
while num <= 20:
    Sum_of_nos += num
    num += 1

print(f"The sum_of_nos from 1 to 20: ", Sum_of_nos)

"""
Print each character of the string "Hello" using a loop.
"""


def character(string):
    for i in range(len(string)):
        print(string[i], end="")
        i += 1
    print()


character("Hello World!")


"""
Create a list of your favorite fruits and print the second fruit on the lis
"""

fruits = ["apple", "orange", "grapes"]
print(fruits[1])

"""
Add the number 7 to a set. Add the number 7 again and observe the set's
behavior.
"""

Set = {1, 2, 3, 4, 5, 6}
Set.add(7)
print(Set)
Set.add(7)
print(Set)

"""
Write a function that takes a list as input and returns a new list without
duplicate elements.
"""

new_list = []


def List1(empty_list):
    global new_list
    for item in empty_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


results = List1(["ABC", 1234, "hemant", "ABC", 3.142, 1234])
print(results)

"""
Create a tuple containing your birth year, birth month, and birth day.
"""

new_tuple = (1996, 2, 15)
print(new_tuple)

"""
Define a function calculate_average that takes a list of numbers as input and
returns their average.
"""

sum_of_nos = 0
num = 1


def calculate_average(average):
    global sum_of_nos
    global num
    for i in range(len(average)):
        sum_of_nos += average[i]
        i += 1
    print(f"The sum of the list:", sum_of_nos)
    print(f"The average of the list:", sum_of_nos/len(average))


calculate_average([1, 2, 3, 4, 5, 6])

"""
Write a function power that takes two arguments, base and exponent , and
calculates base raised to the power of exponent .
"""


def power(base, exponent):
    return base ** exponent  # for checking base to the power we can use "**"


result1 = power(2, 5)
print(result1)

"""
Define a function that takes any number of strings as arguments and returns
them concatenated.
"""
new_lists = ""


def any_strings(string):
    global new_lists
    for items in range(len(string)):
        new_lists += string[items]
    print(new_lists)


any_strings([str(input("Enter a string: "))])


"""
 Check if the word "apple" is present in the string "I like apples and oranges" .
"""

String = "I like apples and oranges"
if "apple" in String:
    print("Present")
else:
    print("Not present")


"""
Count the occurrences of the letter "i" in the string "Mississippi" .
"""


def count_char(letter, char):
    return letter.count(char)


output = count_char(letter=input("Enter the string: "), char=input("Enter the char: "))
print(output)


"""
Reverse the string "Python" using slicing.
"""

Reverse_string = "Python"
print(Reverse_string[::-1])

"""
Create a dictionary representing a car with keys "make" , "model" , and
"year" . Print the car's model.
"""

dictionary = {"make": "tata", "model": "diesel", "year": "2024"}
print(dictionary["model"])

"""
Add a new car to the dictionary, modify the year of an existing car, and
retrieve the make of a specific car.
"""

dictionary["car"] = "BMW"
dictionary["year"] = 2020
print(dictionary)
print(dictionary.get("make"))

