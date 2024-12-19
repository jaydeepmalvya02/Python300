#hourglass
n=7
def Pattern18(n):
    sp=0
    st=n
    for i in range(1,n+1):

        for j in range(1,sp+1):
            print(" ",end="\t")

        for s in range(1,st+1):
            if i>1 and i<=n//2 and s>1 and s<st:
                print(" ",end='\t')
            else:
                print("*",end="\t")

        if i<=n//2:
            sp+=1
            st-=2
        else:
            sp-=1
            st+=2

        print()

Pattern18(n)
