#issubset() - Returns whether another set contains this set or not

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

a={"a","d"}

b= x.issubset(a)
print(b)

#issuperset() Method


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)