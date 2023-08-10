#Recursion
#Python also accepts function recursion, which means a defined function can call itself.

def recursion (k):
    if(k>0):
        result=k+recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion examples :")
recursion(6)