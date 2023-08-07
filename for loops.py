#for loop

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


sports=["cricket","football","basketball","volleyball"]
for x in sports:
    print(x)

#Looping Through a String

for x in "cricket":
    print(x)


#The break Statement

#With the break statement we can stop the loop before it has looped through all the items

for x in sports:
    print(x)
    if (x=="basketball"):
        break