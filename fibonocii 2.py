
x=int(input("Enter the num:"))
a=0
b=1
sum=0
i=0

while(i<x):
    print(" ",+a)
    sum=sum+a
    next=a+b
    a=b
    b=next
    i=i+1
print("\n The Sum of Fibonacci Series no. =%d"%sum)

"""  for x in range (2,6):
        if a<=6:

            s=a+b
            print(s)
            a=a+1
            b=b+1
            s=s+(a+b)
    print()"""