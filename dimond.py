x=int(input("enter a number"))
for i in range (1,x+1):
    print(" "*(x-i),end=" ")
    for j in range (1,i+1):
        print(j,end=" ")
    print()
for i in range (x-1,0,-1):
    print(" "*(x-i),end=" ")
    for j in range (1,i+1):
        print(j,end=" ")
    print()