n=11
def Pattern(n):

    sp=0
    st=n
    for i in range(n):
        for s in range(sp):

            print(" ",end="\t")
        for j in range(st):
            if i>n//2 and i<n-1 and j>0 and j<st-1:
                print("   ",end="\t")
            else:
                print("*",end='\t')

        if i<n//2:
            sp+=1
            st-=2
        else:
            sp-=1
            st+=2
        print()



Pattern(n)