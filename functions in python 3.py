#Passing a List as an Argument

def func(food):
    for x in food:
        print(x)
fruits=["Apple","Mango","Guava","Cherry"]
func(fruits)

#Return Values
#To let a function return a value, use the return statement:

def func(x):
    return 5*x
print(func(3))
print(func(5))
print(func(4))

#pass Statement

#function definitions cannot be empty, but if you for some reason have a function definition with
# no content,put in the pass statement to avoid getting an error.

def func():
    pass