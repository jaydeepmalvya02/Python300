mat=[
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44]
]

n=len(mat)
m=len(mat[0])
#transporse
for i in range(n):
    for j in range(i,n):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

#col Swap
for i in range(n):
    l=0
    r=n-1
    while l<r:
        mat[i][l],mat[i][r]=mat[i][r],mat[i][l]
        l+=1
        r-=1

print(mat)