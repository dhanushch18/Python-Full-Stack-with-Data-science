sports=["cricket","football","basketball"]
print(sports)

x=sports[1]
print(x)

#Length of an Array
x=(len(sports))
print(x)

#Looping Array Elements

for x in sports:
    print(x)

#Adding Array Elements
sports=["cricket","basketball","football"]
sports.append("baseball")
print(sports)

#Removing Array Elements

sports.remove("cricket")
print(sports)

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""