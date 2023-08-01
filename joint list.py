l1=["a","b","z","x"]
l2=[17,19,18,7]
l3=l1+l2
print(l3)

#Append list2 into list1:
"""l1=["a","b","z","x"]
l2=[17,19,18,7]"""
for x in l2:
    l1.append(x)

print(l1)

#use the extend() method, where the purpose is to add elements from one list to another list

l1.extend(l2)
print(l1)

#list methods

#append()	Adds an element at the end of the list
"""clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""