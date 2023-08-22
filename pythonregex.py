#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

#RegEx can be used to check if a string contains the specified search pattern.

#Search the string to see if it starts with "The" and ends with "Spain":

import re

txt="The rain is in Spain"
x=re.search("^The.*Spain$",txt)

if x:
    print("Yes,we have a match")
else:
    print("No")

"""
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

import re

txt="The rain is in Spain17"

##Find all lower case characters alphabetically between "a" and "m":

x=re.findall("[a-s]",txt)
print(x)
#Find all digit characters:

x=re.findall("\d",txt)
print(x)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x=re.findall("r..n",txt)
print(x)

#Check if the string starts with 'the':

x=re.findall("^The",txt)
if x:
    print("yes")
else:
    print("no")

##Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
import re

txt = "hello planet"
x = re.findall("he.{2}o", txt)

print(x)


import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
