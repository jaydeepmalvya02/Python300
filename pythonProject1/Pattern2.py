n=int(input("enter range"))
for i in range(0,n):
    for j in range(n-i-1):
        print('-',end="\t")
    for k in range(i+1):
        print("*", end="\t")
    print()