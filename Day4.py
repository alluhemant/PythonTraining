"""String Concatenation"""
a = "Genzeon" + " " + "Technology"
print(a)

"""Possible Mistakes
adding string with integer 
a = "Hello" + 10 
print(a)
"""
print("Hemant".upper())

"""String repetetion"""
a = "Genzeon" * 5
print(a)

s = "Bike"
s = ("* " * 3) + s + (" *" * 3)
print(s)

"""Length Of String"""
name = input()
length = len(name)
print(length)

"""Concatenate two strings str1 and str2 , 
and print the result."""
str1 = "Genzeon"
str2 = "Technology"
print(str1 + str2)

""" Ask the user to enter their name and a greeting. 
Concatenate the name and
greeting to form a personalized message and print it"""
name = input("Enter your name: ")
greeting = input("Enter a greeting: ")
print(name + " " + greeting)

"""Create a string word and repeat it 5 times. 
Print the result."""
word = "python"
print(word * 5)

"""Create a string sentence and 
find its length. Print the length of the sentence.
"""
sentence = "Genzeon"
print(len(sentence))

"""Ask the user to input a sentence. 
Find the length of the sentence, and print
the last character of the sentence."""

my_sentence = input("Enter Sentence: ")
length = len(my_sentence)
print("The length of the string is: ", length, "and", "last Character of sentence is: ", my_sentence[length-1])

""" Create two strings str1 and str2 . Find the lengths of both strings and
concatenate them. 
Print the concatenated string."""

"""Ask the user to enter two words, 
word1 and word2 . Concatenate the two
words with a space in between and print the result."""

"""Create a string pattern containing "*" character and repeat it to form a
pattern. The pattern should have 5 rows. 
Print the resulting pattern."""

pattern = "*"
for i in range(6):
    print("*" * i)
