i=1
for i in range (5):
    k=1
    for k in range(5-i):
        print('',end="  ")

    for j in range (i+1):
        print("*",end="  ")
    print("\n")

    # i=i+1
