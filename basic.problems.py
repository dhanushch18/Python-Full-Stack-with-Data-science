#add 2 num

#sum


x=int(input("Enter a number :"));

y=int(input("Enter a number :"));
c=(x+y);

print(c)


#hello world

print("Hello World")


#square root

n=int(input("Enter a num :"));

x=n**(1/2);
print("The square root is",+x);



#Area of a triangle

l=int(input("Length is :"));
b=int(input("Width is :"));
a=((l*b)/2);
print("Area =",+a);


#swapping

a=int(input("Enter a num a:"));
b=int(input("Enter a num b:"));
c=a;
a=b;
b=c;
print("a =",+a);
print("b =",+b);


#km to miles

k=float(input("Enter the km :"));
m=(0.621371)*k;
print(k,"km in miles will be",m,"miles");


#check a num is +,-,or 0

n=int(input("Enter a num : "));
if(n==0):
    print("The value is zero");
elif(n>0):
    print("The value is positive");
else:
    print("The value is negative");


#find even or odd num.

n=int(input("Enter a num : "));
if(n%2==0):
    print("Num is even")
else:
    print("Num is odd")


#leap year

n=int(input("Enter a num : "));
if(n%100==0) and (n%400==0):
    print("Leap year")
elif (n%4==0) and (n%100!=0):
     print("Leap year")
else:
    print(n,"Not a leap year")


#largest num

x=int(input("Enter a num : "));
y=int(input("Enter a num : "));
z=int(input("Enter a num : "));
if(x>y)and(x>z):
    print(x," is the largest num.");
if(y>x)and(y>z):
    print(y," is the largest num.");
else:
    print(z," is the largest num.")


#prime num

n=int(input("Enter a num :"));

if (n==1):
    print(n,"it is not a prime num");
if n>1:
    for i in range(2,n):
        if n % i ==0:
            print("it is not a prime num");
            break
    else:
        print("it is a prime num");


#random num

import random
n=random.randint(1,6)
print(n)