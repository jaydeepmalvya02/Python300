def Pattern17(n):

    nsp=n//2
    nst=1
    i=0

    while i<=n:
        s=1
        while s<=nsp:
            if i==n//2:
                print("*",end='\t')
            else:
                print("",end="\t")
            s+=1
        st=1
        while st<=nst:
            print("*",end=" ")
            st+=1

        if i<n//2:
            nst+=1
        else:
            nst-=1

        i+=1
        print()


n=4
Pattern17(n)