#Convert the tuple into a list change the list, and convert the list back into a tuple.

x=("virat","abd","cr","ch")
y=list(x)
y[3]="yuvi"
x=tuple(y)
print(x)

#Add Items

#Convert the tuple into a list, add "orange", and convert it back into a tuple:

y.append("msd")
x=tuple(y)
print(x)

#Remove Items

y.remove("yuvi")
x=tuple(y)
print(x)

#Unpacking a Tuple

# in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

actors=("vijay","mohanlal","surya","nivin","dq","mamootty")
(a,b,c,d,e,f)=actors
print(a,b,c,d,e,f)

#Using Asterisk*

(a,b,c,*Mallu)=actors
print(a,b,c,"\n",*Mallu)