def func(n):
    return lambda a:a*n
x=func(4)
print(x(6))

def func(n):
    return lambda a:a*n
x=func(6)
print(x(9))

def func(n):
    return lambda a:a*n
x=func(8)
y=func(9)
print(x(5))
print(y(6))