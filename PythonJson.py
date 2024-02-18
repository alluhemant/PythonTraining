"""
Python has a builtin package called JSON
which can be used to work with JSON data
"""

import json

"""
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
"""

# Converting from JSON to pyhton

x = '{"name": "Hemant", "age": 28, "city": "Hubli"}'

# Parse x
y = json.loads(x)

# Result is a python dictionary
print(y["age"])

# Convert from Python to JSON

x = {
    "name": "Kumar",
    "age": 27,
    "city": "Hyd"
}

# Convert into json

y = json.dumps(x)

# Result is JSON string
print(y)

"""
convert Python objects of the following types, into JSON strings:
dict, list, tuple, string, int, float
True, False, None
"""

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


"""
Python objects are converted into the JSON (JavaScript) equivalent:

dict	Object
list	Array
tuple	Array
str	    String
int	    Number
float	Number
True	true
False	false
None	null

"""


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# If we want to format the result
print(json.dumps(x,indent=4))

# We can separators default value is (",",": ")

json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result
# Use the sort_keys parameters to specify if the result should be sorted or not

print(json.dumps(x, indent=4, sort_keys=True))

