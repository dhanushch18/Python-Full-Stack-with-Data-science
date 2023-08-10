a, b = 4,2

x=int(input("Enter a num :"))

def func(x):
    if(x==1):
        sum = a+b
        print("Add:",+sum)
    elif (x==2):
        diff=a-b
        print("Sub:",+diff)
    elif (x==3):
        mult=a*b
        print("Multiplication:",+mult)
    elif (x==4):
        div=a/b
        print("Division:",+div)
    else:
        print("Invalid")
func(x)

#func(sum1(x,y))
