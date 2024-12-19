def Pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):

            print("*",'\t',end='')
        print()
n=int(input("Enter Range"))
Pattern(n)
