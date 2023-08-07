#continue Statement

#With the continue statement we can stop the current iteration of the loop, and continue with the next:


sports=["cricket","football","basketball","volleyball"]

for x in sports:

    if (x=="football"):
        continue
    print(x)

#range() Function

for x in range(9):
    print(x)

for x in range(11,20):
    print(x)

#Increment the sequence with 2

for x in range (2,15,2):
    print(x)

#Else in For Loop

for x in range (8):
    print(x)
else:
    print("finished")

#Break the loop when x is 3

for x in range (7):
    if x==6:break
    print(x)
else:
    print("Finished")

#Nested Loops
#A nested loop is a loop inside a loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)