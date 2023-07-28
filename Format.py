#String Format

age=22
txt = "My name is ch,and I am {} years old"
print(txt.format(age))


#more variables

quantity=7
itemno=17
price=77
myorder="I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity, itemno , price))


myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

myorder = " I have a {bike},of {model} "
print(myorder.format(bike = "Royal Enfield", model = "Clasic350"))

