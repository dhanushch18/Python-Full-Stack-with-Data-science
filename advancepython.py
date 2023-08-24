#class

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("Dhanush",22)

print(p1.name)
print(p1.age)


#string

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"My name is {self.name},and I'm {self.age}"

p1=person("CH17",22)
print(p1)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("Hello my name is "+self.name,+self.age)
p1=person("dhanush",22)
p1.func()
