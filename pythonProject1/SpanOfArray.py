#difference btw max and min
n=int(input('Enter the len of array'))
a=list(map(int,input().split()))
min=a[0]
max=a[0]
for i in range(1,n):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]

Span=max-min
print(Span)


