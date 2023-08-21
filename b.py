import aa

aa.greeting("Jonathan")

import aa
x=aa.person1
y=aa.person1["age"]
print(x)
print(y)

#Re-naming a Module

import aa as mod

z=mod.person1
print(z)


#Built-in Modules

import platform

x=platform.system()
print(x)

y=platform.architecture()
print(y)

#Using the dir() Function

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import platform
x=dir(platform)
print(x)

#Import From Module

from aa import person1

print (person1["age"])