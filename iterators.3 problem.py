#doubling the values

class num:
    def __iter__ (self):
        self.a=2
        return self
    def __next__(self):
        x=self.a
        self.a+=x
        return x
myclass=num()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))