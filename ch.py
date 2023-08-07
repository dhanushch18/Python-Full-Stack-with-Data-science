#palindrome

num=int(input("Enter a num:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
        print("The {0} is a palindrome ".format(temp))
else:
        print("Not a palindrome")