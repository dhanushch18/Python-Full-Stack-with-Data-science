#Python Scope

#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the
#local scope of that function, and can only be used inside that function.

def func():
    x=500
    print(x)
func()

#

def func():
    x=700
    def innerfunc():
        print(x)
    innerfunc()
func()

#Global Scope

#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.

x=999

def func():
    print(x)
func()
print(x)

x=777
def func():
    x=666
    print(x)
func()
print(x)

#Global Keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.

def func():
    global x
    x=300
func()
print(x)

#this will not check outside variable

x=444
def func():
    global x
    x=200
func()
print(x)

