s="Abc"
n=len(s)
def Permutation(s,n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    for i in range(fact):
        tmp=i
        ans=s
        for j in range(n,0,-1):
            rem=tmp%j
            tmp=tmp//j
            print(ans[rem],end="")
            ans=ans[0:rem]+ans[rem+1:]
        print()

Permutation(s,n)


