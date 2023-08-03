#difference() -	Returns a set containing the difference between two or more sets

x={"ch","vk18","abd17"}
y={"msd","abd17","yuzi"}

z = x.difference(y)
a=y.difference(x)
print(z,"\n",a,"\n")

#difference_update() - Removes the items in this set that are also included in another, specified set

x.difference_update(y)
print(x)