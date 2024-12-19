R=int(input("enter range"))
C=int(input("Enter range:"))
ans=[]
b=1
for i in range(R):
    a=[]

    for j in range(C):

        a.append(b)
        b+=1
    ans.append(a)

for i in range(R):
    for j in range(C):
        print(ans[i][j],end=' ')
    print()
