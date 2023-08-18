#The __str__() Function
#The __str__() function controls what should be returned when the class object is represented as a string.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"
p1=person("Dhanush",22)
print(p1)

#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("Hello I'm " +self.name,"and I'm "+self.age)
p1=person("Dhanush","seven")
p1.func()

#The self Parameter

#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

#It does not have to be named self ,
# you can call it whatever you like, but it has to be the first parameter of any function in the class:

class person:

 def __init__(myobject,name,age):
    myobject.name=name
    myobject.age=age
 def func(abd):
    print("His name is "+abd.name)
p1=person("ch",22)
"""p1.age=25
print(p1.age)"""
p1.func()

#Modify Object Properties

p1.name="abd"
print(p1.name)

p1.age=25
print(p1.age)

#Delete Object Properties
#You can delete properties on objects by using the del keyword:

del p1.age
print(p1.age)
del p1

#Delete Objects
#You can delete objects by using the del keyword:

del p1
print(p1)

#The pass Statement

#class definitions cannot be empty, but if you for some reason have a
# class definition with no content, put in the pass statement to avoid getting an error.

class person:
    pass