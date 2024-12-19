arr=[
    [11,15,17,18,20],
    [25,29,30,35,45],
    [47,49,50,51,52],
    [48,60,62,68,70],
    [65,70,71,72,73]
]
n=5
k=68
i=0
j=n-1
ans=[]
while i<n or j>=0:

    if arr[i][j]==k:
        print(i)
        print(j)
        break
    elif arr[i][j]<k:
        i+=1
    else:
        j-=1
