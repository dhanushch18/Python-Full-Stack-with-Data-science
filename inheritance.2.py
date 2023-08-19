class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student (person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

x= student("dhanush","ch",2017)
x.printname()
print (x.graduationyear)


#add methods
#Add a method called welcome to the Student class:

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
            print("I am ",self.firstname,self.lastname,"living in the year",self.graduationyear)
x= student("dhanush","ch17",2023)
x.welcome()