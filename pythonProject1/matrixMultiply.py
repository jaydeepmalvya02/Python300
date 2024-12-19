def MatrixMul(n1,n2,m1,m2,mat1,mat2):
    r = n1
    c = m2
    if m1!=n2:
        print("false")

    ans1=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(0)
        ans1.append(a)


    for i in range(r):
        for j in range(c):
            s=0
            for k in range(m1):
                s+=mat1[i][k]*mat2[k][j] #formula for calculate matrix index value
            ans1[i][j]=s

    for i in range(r):
        for j in range(c):
            print(ans1[i][j],end=" ")

        print()









n1=2
n2=3
m1=3
m2=4
mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2,3,4],[4,5,6,7],[7,8,9,7]]
MatrixMul(n1,n2,m1,m2,mat1,mat2)