# Use a Module

import sample
import sample as sp
from sample import person1

sample.greeting("Hemant")

a = sample.person1["age"]
print(a)

# Using module as alias

sp.greeting("Kumar")

a = sp.person1["name"]
print(a)

# Import from module

print(person1["country"])

