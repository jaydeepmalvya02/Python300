n=int(input("enter range:"))
sp=n//2
st=1
for i in range(1,n+1):

    for j in range(sp+1):
        print('*',end="\t")

    for k in range(st+1):
        print(' ',end='\t')
    for j in range(sp+1):
        print('*',end="\t")


    if i<=n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2

    print()