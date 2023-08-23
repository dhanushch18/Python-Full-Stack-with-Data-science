#String format()

#The format() method allows you to format selected parts of a string.

price=99
txt="The price is {} rupees"
print(txt.format(price))

#Format the price to be displayed as a number with two decimals:

txt="The price is {:.2f} rupees"
print(txt.format(price))

#Multiple Values

quantity=3
itemno=99
price=777
order="I want {} pieces of item no. {} for {:.2f} rupees"
print(order.format(quantity,itemno,price))

#Index Numbers
quantity=5
itemno=90
price=7777
order="i want {0} pieces of item no. {1} for {2:.2f} rupees"
print(order.format(quantity,itemno,price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#if you want to refer to the same value more than once, use the index number:

age=22
name="Dhanush"
txt="His name is {1}.{1} is {0} years old."
print(txt.format(age,name))

#Named Indexes

order="I have a {carname}, it is a {model}"
print(order.format(carname="Tata",model="Tiago"))