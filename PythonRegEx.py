"""
A RegEx, or Regular Expression, is a sequence
of characters that forms a search pattern.

RegEx can be used to check
if a string contains the specified search pattern.
"""

import re

string = "Hello World!"
x = re.search("H.*W", string)
print(x)

print(re.findall("l", string))
print(re.search("o", string))
print(re.split("W", string))
print(re.sub("l", "I", string))

"""  Metacharacters

Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group

"""

