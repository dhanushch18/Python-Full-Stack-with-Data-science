"""Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

The __iter__() method acts similar, you can do operations (initializing etc.),
 but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence."""

#problem
#Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class num:
    def __iter__ (self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=num()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
