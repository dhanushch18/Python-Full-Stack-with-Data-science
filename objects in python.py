#A Class is like an object constructor, or a "blueprint" for creating objects.

class myclass:
    x=7
p1=myclass()
print(p1.x)

#The __init__() Function

#All classes have a function called __init__(), which is always executed when the class is being initiated.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("Dhanush",22)
print(p1.name)
print(p1.age)