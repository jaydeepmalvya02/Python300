n=5
def Pattern(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i>=n//2  and ( j==i or i==n-1-j):
                print("*",end="\t")

            else:
                print("",end='\t')
        print()

Pattern(n)