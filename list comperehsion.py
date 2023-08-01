l1=["apple","mango","kiwi","melon","strawberry"]
l2=[]
for x in l1:
    if "a" in x:
        l2.append(x)

print(l2)

# one line of code:
l4=["abc","abd","vk18","ch17","ak#"]
l3=[ x for x in l4 if "a" in x]
print(l3)

#Only accept items that are not "apple":

l5=[x for x in l3 if x!="abc"]
print(l5)

#iterable
#range() function to create an iterable:

l6=[x for x in range(18)]
print(l6)

#Accept only numbers lower than 5:

l7=[x for x in range (18) if x<5]
print(l7)

# new list to upper case:

l8=[x.upper() for x in l1]
print(l8)

#Return "orange" instead of "banana":

l9=[x if x != "apple" else "orange" for x in l1]
l10=[x.upper() for x in l9]
print(l10)