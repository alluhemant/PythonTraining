"""
try:
    blocks lets you test a block of code for errors.

except:
    block lets you handle the error.

else:
    blocks lets you execute code when there is no error.

finally:
    block lets execute a code regardless of result
    of try and except blocks.
"""

# Example:
# x = 5
try:
    print(x)
except:
    print("variable is not defined")

# Without try block it raises an error

# print(x)

# Many Exceptions
x=5
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Other errors")

# ELSE block

try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("nothing went wrong")

# Finally block
# This can be useful to close objects
# and clean up resources:

try:
    print(y)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Hemant")
    except:
        print("Went wrong while writing the file")
    finally:
        f.close()
except:
    print("went wrong while opening the file")

# Raise an exception
"""
you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, 
use the raise keyword.



x = -1
if x < 0:
    raise Exception("Number is below zero")
"""

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
