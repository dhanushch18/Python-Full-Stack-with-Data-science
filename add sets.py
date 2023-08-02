set={"virat","msd","abd","ch"}

set.add("orange")
print(set)
set2={"yuvi","cr"}
set.update(set2)
print(set)

#Add Any Iterable

#update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).\

set3=["yuzi","dhanush"]

set.update(set3)
print(set)