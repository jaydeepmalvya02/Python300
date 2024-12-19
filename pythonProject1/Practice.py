
#SpiralMatrix
mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n=3
m=3
t=m*n
count=0
minc=0
minr=0
maxc=m-1
maxr=n-1
ans=[]

while count<t:
    #top
    i=minr
    j=minc
    while j<=maxc and count<t:
        ans.append(mat[i][j])
        j+=1
        count += 1


    minr+=1


    #right
    i=minr
    j=maxc
    while i<=maxr and count<t:

        ans.append(mat[i][j])
        i+=1
        count+=1
    maxc-=1
    #bottom
    i=maxr
    j=maxc
    while j>=minc and count<t:
        ans.append(mat[i][j])
        j-=1
        count+=1
    maxr-=1
    #left
    i=maxr
    j=minc
    while i>=minr and count<t:
        ans.append(mat[i][j])
        i-=1
        count+=1
    minc+=1


print(ans)













#
# #exitPoint
# arr=[
#     [0,0,0,1],
#     [1,0,0,0],
#     [0,0,1,0],
#     [0,0,0,1]
# ]
# m=4
# n=4
# t=n*m
# count=0
# dir=0
# i=0
# j=0
# while count<t:
#     dir=(dir+arr[i][j])%4
#     count+=1
#     # 0=>east->
#     if dir==0:
#         j+=1
#         if j==m:
#             j-=1
#             break
#     #1=>south
#
#     elif dir==1:
#         i+=1
#         if i==m:
#             i-=1
#             break
#     elif dir==2:
#         j-=1
#         if j==-1:
#             j+=1
#             break
#     elif dir ==3:
#         i-=1
#         if i==-1:
#             i+=1
#             break
#
# print(i,j)
#
































# n=int(input("n1:"))
# # n2=int(input("n2:"))
# b=int(input("base:"))

# def AddToAny(n1,n2,b):
#     pow=1
#     ans=0
#     carry=0
#     while n1>0 and n2>0 or carry>0:
#         d1=n1%10
#         d2=n2%10
#         t=d1+d2+carry
#         carry=t//b
#         rem=t%b
#         ans+=rem*pow
#         pow*=10
#         n1=n1//10
#         n2=n2//10
#     print(ans)
#
#
#
# AddToAny(n1,n2,b)

# def AnytoAny(n,b):
#     ans=0
#     pow=1
#     while n>0:
#         d=n%b
#
#         ans+=d*pow
#         n=n//b
#         pow=pow*10
#
#     print(ans)
# AnytoAny(n,b)4
# def AnyToDec(n,b):
#     ans=0
#     pow=1
#     while n>0:
#         rem=n%10
#         ans+=rem*pow
#         pow*=b
#         n=n//10
#     print(ans)
#
# AnyToDec(n,b)
# def DecToAny(n,b):
#     ans=0
#     pow=1
#     while n>0:
#         rem=n%b
#         ans+=rem*pow
#         pow*=10
#         n=n//b
#     print(ans)
# DecToAny(n,b)

# def binToany(n,b):
#     ans=0
#     pow=1
#     while n>0:
#         rem=n%10
#         ans+=rem*pow
#         pow*=2
#         n=n//8
#     print(ans)
# binToany(n,b)