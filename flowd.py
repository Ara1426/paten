x=int(input("enter a number"))
number=1
for i in range(x):
    for h in range(i+1):
        print(number,end=" ")
        number=number+11
    print()