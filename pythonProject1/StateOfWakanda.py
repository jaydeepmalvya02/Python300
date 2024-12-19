mat1=[[1,2,3,1],
      [4,5,6,2],
      [7,8,9,3]]
n=3
c=4
for i in range(c):
    if i % 2 == 0:
        for j in range(n):
            print(mat1[j][i],end='->')
    else:
        for j in range(n-1,-1,-1):
            print(mat1[j][i],end="->")