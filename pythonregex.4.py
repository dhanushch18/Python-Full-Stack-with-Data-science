#The findall() Function
#The findall() function returns a list containing all matches.

import re
x="I love rain in India"
x=re.findall("in",x)
print(x)

#The search() Function

#The search() function searches the string for a match, and returns a Match object if there is a match

#Search for the first white-space character in the string:

import re

txt="The rain in spain"
x=re.search("\s",txt)
print(x.start())

#If no matches are found, the value None is returned:

y=re.search("portugal",txt)
print(y)


#The split() Function

#The split() function returns a list where the string has been split at each match:

#Split at each white-space character:

import re

txt="The rain in spain"
x=re.split("\s",txt)
print(x)

#Split the string only at the first occurrence:

x=re.split("\s",txt,2)

print(x)

#The sub() Function

#The sub() function replaces the matches with the text of your choice:

#Replace every white-space character with the number 9:

x=re.sub("\s","7",txt)
print(x)

#Replace the first 2 occurrences:

x=re.sub("\s","7",txt,1)
print(x)

#Match Object

#A Match Object is an object containing information about the search and the result.

#Do a search that will return a Match Object:

x=re.search("ai",txt)
print(x)

"""

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match

"""

x=re.search(r"\bs\w+",txt)
print(x.span())

import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
