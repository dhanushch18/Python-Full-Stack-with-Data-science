#find leap year

#x=2024

x=int(input("enter a num:"))

if(x%400==0) and (x%100==0):
    print("x is a leap year")
elif((x%4==0) and (x%100!=0)):
    print("x is a leap year")

else:
    print("x is not a leap year")