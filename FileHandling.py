# Python File open

"""
open() take 2 parameters filename, and mode.
There are 4 different methods(modes) for opening file

"r" - Read --> Default value
"a" - Append --> Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

# f = open("demofile.txt") error

# f = open("demofile.txt", "rt")  --> r = Read and t = "text" default values

# Creating the file
# f = open("demofile.txt", "x")

# Reading the file

f = open("demofile.txt", "r")
print(f.read())

"""
If the file is located in a different location, you will have to 
specify the file path:
"""

# read 5 characters from file
f = open("demofile.txt","r")
print(f.read(5))

# Read Lines
# We can return one line by using readline() method.

f = open("demofile.txt","r")
print(f.readline(), f.readline())


f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()


"""
Write to an Existing File

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""

f = open("demofile.txt","a")
f.write(f"\n Now the file has some more lines")
f.close()

# Ove ridding the file content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

# Create a file called "myfile.txt":

# f = open("myfile.txt", "x")

"""
Delete a File
To delete a file, you must import the OS module, 
and run its os.remove() function:

"""

import os
# os.remove("myfile.txt")

# Check if file exists,
# then delete it:

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

# Remove the folder "myfolder":

# import os
# os.rmdir("myfolder")
