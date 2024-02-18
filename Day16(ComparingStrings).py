string1 = "hello"
string2 = "Hello"

if string1 == string2:
    print("Both are equal.")
else:
    print("Strings are not equal")

if string1 != string2:
    print("Strings are not equal")
else:
    print("Both are equal.")

# Example: Lexicographical comparison
string1 = "apple"
string2 = "banana"

if string1 < string2:
    print("String1 comes before String2")
else:
    print("String1 comes after or is equal to String2.")

if string1 <= string2:
    print("String1 comes before or is equal to String2")
else:
    print("string1 comes after string2.")

if string1 > string2:
    print("string1 comes after string2.")
else:
    print("string1 comes before or is equal to string2.")
if string1 >= string2:
    print("string1 comes after or is equal to string2.")
else:
    print("string1 comes before string2.")