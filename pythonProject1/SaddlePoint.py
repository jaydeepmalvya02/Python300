arr=[
    [2,13,5,6],
    [13,11,15,19],
    [3,25,2,1],
    [6,12,5,2]
]

n=4

col=0
for i in range(n):
    a = arr[i][0]
    j=1

    while j<n:
        if arr[i][j]<a:
            a=arr[i][j]
            col=j

        j+=1

k=0
while k<n:
    if a<arr[k][col]:
        break
    k+=1
k+=1
if k==n:
    print(a)
else:
    print("-1")

