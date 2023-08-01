#sort() method that will sort the list alphanumerically, ascending, by default

l1=["chikku","apple","mango","kiwi","melon","strawberry"]
l1.sort()
print(l1)

#Sort the list numerically:

l2=[1111,999,111,18,19,17]
l2.sort()
print(l2)

#Sort Descending
"""sort descending, use the keyword argument reverse = True:"""

l1.sort (reverse = True)
print(l1)

#Customize Sort Function

#customize your own function by using the keyword argument key = function.

#how close the number is to 50:

def myfun(n):
    return abs(n-50)
l1=[100,75,11,17,50,99]
l1.sort(key = myfun)
print(l1)

#Case Insensitive Sort

#sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

l3=["chikku","apple","Mango","kiwi","melon","Strawberry"]
l3.sort()
print(l3)
l3.sort(key = str.lower)
print(l3)

#Reverse Order

l3.reverse()
print(l3)
