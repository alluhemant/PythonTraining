"""
Create a variable name and assign your name to it. Print a message using
the variable, such as: "Hello, [name]!"
"""

name = "Hemant"
print(f"Hello, {name}!")

"""
Convert the string "37" to an integer and assign it to a variable num . Print
the value and type of num 
"""

String_num = "37"
print(type(String_num))
Integer_num = int(String_num)
print(type(Integer_num))

"""
Define a tuple with four elements: "apple" , "banana" , "cherry" , and "date" .
Print the second element.
"""

Tuple = ("apple", "banana", "cherry", "date")
print(Tuple[1])


"""
Swap the values of two variables, x and y , without using a temporary
variable.
"""

X = 5
Y = 10
temp = X
X = Y
Y = temp
print(X, Y)

"""
Write a program that takes your age as input and prints a sentence like: "You
are [age] years old."
"""


def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]


# Driver Program
print(fibonacci(9))


