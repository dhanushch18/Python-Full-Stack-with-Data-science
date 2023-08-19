#StopIteration
#The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
#To prevent the iteration from going on forever, we can use the StopIteration statement.

#problem - Stop after 20 iterations:


class num:
    def __iter__ (self):
        self.a=2
        return self
    def __next__(self):
       if self.a <=20:
           x=self.a
           self.a+=1
           return x
       else:
           raise StopIteration

myclass=num()
myiter=iter(myclass)
for x in myiter:
    print(x)


#if else statement and stop iteration not given it will go on printing "none" statement after looping.
"""class num:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        #else:
         #   raise StopIteration


myclass = num()
myiter = iter(myclass)
for x in myiter:
    print(x)
"""