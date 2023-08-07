#palindrome

num=int(input("Enter any number:"))
a=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(a==rev):
    print("The {0} number is palindrome".format(a))
else:
    print("Not a palindrome")