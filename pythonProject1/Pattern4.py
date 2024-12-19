n=int(input("enter Rang"))

for i in range(n):
    for j in range(i):
        print("-",end="\t")
    for k in range(n-i):
        print("*",end='\t')
    print()
