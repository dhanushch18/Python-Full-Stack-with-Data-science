#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    pass
x=student("Virat","Gayle")
x.printname()


class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def printname(self):
        print(self.name,self.id)
class student(person):
    def __init__(self,name,id):
        person.__init__(self,name,id)

x=student("Dhanush","ch")
x.printname()


#Python also has a super() function that will make
# the child class inherit all the methods and properties from its parent:


class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def printname(self):
        print(self.name,self.id)
class student(person):
    def __init__(self,name,id):
        super().__init__(name,id)

x=student("Dhanush","ch17")
x.printname()

#add properties

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Masker", "boy")
x.printname()
print(x.graduationyear)

