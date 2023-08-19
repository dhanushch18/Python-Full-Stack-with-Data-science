#Python Iterators

#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#__iter__() and __next__().

#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

tuple=("cricket","football","golf")
sports=iter(tuple)

print(next(sports))
print(next(sports))
print(next(sports))

#Even strings are iterable objects, and can return an iterator:
# in list

list=["dhanush"]
name=iter(list)

print(next(name))



list="dhanush"
name=iter(list)

print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))


#Looping Through an Iterator

tuple=("apple","banana","mango")
for x in tuple:
    print(x)

set="dhanush"
for x in set:
    print(x)