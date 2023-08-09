#Keyword Arguments
#You can also send arguments with the key = value syntax.

def func(name1,name3,name2):
    print("The eldest boy is "+name2)
func(name1="dhanush",name2="virat",name3="sachin")


#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

def func(**name):
    print("His name is "+name["name1"])
func(name1="dhanush",name2="ch")