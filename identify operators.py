#is  Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = y

print ( x is z )
print ( x is y )
print ( x == z )

#is not  Returns True if a sequence with the specified value is not present in the object

print(x is not z,x is not y, x==y)