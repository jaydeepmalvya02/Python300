def BarChart(a,b):

    for i in reversed(range(1,b+1)):
        for j in range(n):
            if a[j]>=i:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    pass

n=int(input("no of Elements:"))
a=list(map(int,input("Enter the  elements").split()))
b=max(a)
BarChart(a,b)

