#Python Polymorphism

#The word "polymorphism" means "many forms", and in programming it refers
# to methods/functions/operators with the same name that can be executed on many objects or classes.

#len()
#string
x=("dhanush")
print(len(x))

#tuple

car=("benz","bmw","ferrari")
print(len(car))

#dictionary

sports={
    "cricket":"virat",
    "football":"ronaldo"
}
print(len(sports))

#class polymorphism

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")


car1 = car("lamborgini", "huraccan")       #Create a Car class
boat1 = boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = plane("Boeing", "747")     #Create a Plane class

for x in (plane1,car1,boat1):
    x.move()


#inheritance class polymorphism

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")
class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("sail")

class plane(vehicle):
    def move(self):
        print("fly")

car1 = car("Ford", "Mustang") #Create a Car object
boat1 = boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = plane("Boeing", "747") #Create a Plane object

for x in (plane1,boat1,car1):
    print(x.brand)
    print(x.model)
    x.move()