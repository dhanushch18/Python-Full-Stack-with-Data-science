#Sets
#A set is a set of characters inside a pair of square brackets [] with a special meaning

"""
[arn]	Returns a match where one of the specified characters (a, r, or n) is present
[a-n]	Returns a match for any lower case character, alphabetically between a and n
[^arn]	Returns a match for any character EXCEPT a, r, and n
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	Returns a match for any digit between 0 and 9
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

import re

txt="spain is a country"

##Check if the string has any a, r, or n characters:

x=re.findall("[arn]",txt)
print(x)
y=re.findall("[a-n]",txt)
print(y)
z=re.findall("[^asn]",txt)
print(z)

txt = "8 times before 11:45 AM"
x=re.findall("[0-9]",txt)
print(x)

