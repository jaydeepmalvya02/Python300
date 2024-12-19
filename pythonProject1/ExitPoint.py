matrix=[
    [0,1,0,0],
    [1,0,0,1],
    [0,0,0,1],
    [1,1,1,0]
]
m=4
n=4

dir=0
i=0
j=0
t=n*m
count=0
while count<t:
    #dir
    dir=(dir+matrix[i][j])%4
    count+=1

    #dir==0 ->east
    if dir==0:
        j+=1
        if j==m:
            j-=1
            break
    #dir==1 ->south
    elif dir==1:
        i+=1
        if i==n:
            i-=1
            break
    #dir==2->west
    elif dir==2:
        j-=1
        if j==-1:
            j+=1
            break
    #dir==3 ->North
    else:
        i-=1
        if i==-1:
            i+=1
            break
print(i,j,end=" ")
