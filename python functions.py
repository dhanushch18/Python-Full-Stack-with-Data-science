#function
#A function is a block of code which only runs when it is called.

def function():
    print("Hello from a function" )
function()

#Arguments
#Information can be passed into functions as arguments.

def func(name):
    print(name + "ch17")
func("dhanush")
func("virat")
func("abd")


def func(name,age):
    print(name+" 7 " +age)
func("dhanush","#22")
func("cr","#38")


def sum(a,b):
    sum1=a+b
    return sum1
print(sum(2,3))

#another method
def sum(a,b):
    sum1=a+b
    return sum1
t=sum(2,3)
print(t)

#Arbitrary Arguments, *args
#If the number of arguments is unknown, add a * before the parameter name:

def func(*name):
    print("youngest is " +name[2])
func("dhanush","abd","vk","yuzi")


