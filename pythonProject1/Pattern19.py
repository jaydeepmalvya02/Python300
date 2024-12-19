n=9
def Pattern(n):
    for i in range(n//2+1):
        for j in range(n//2+1):
            if  i<n//2 and j<n//2 and j>0:
                print(" ",end='\t')

            else:
                print("*",end='\t')
        for k in range(n//2+1,n):
            if  i<n//2 and i>0:
                print(" ",end='\t')
            else:
                print('*',end='\t')

        print()
    for i in range(n // 2 + 1,n):
        for j in range(n // 2 + 1):
            if i > (n//2)  and i<n-1 and j<n//2:
                print(" ", end='\t')

            else:
                print("*", end='\t')

        for k in range(n//2+1,n):
            if  k<n-1:
                print(" ",end='\t')
            else:
                print("*",end="\t")

        print()



Pattern(n)