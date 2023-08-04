#to check largest num amoung 3 numbers

x=input("enter a num:")
y=input("enter a num:")
z=input("enter a num:")

if(x>=y) and (x>=z):
    print("x is greatest no.")
elif(y>=x) and (y>=z):
    print("y is greatest")
else:
    print("z is greatest")