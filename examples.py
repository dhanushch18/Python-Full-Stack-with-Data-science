i=1
while i <=5:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1


#iterator

x="dhanush"
y=iter(x)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
