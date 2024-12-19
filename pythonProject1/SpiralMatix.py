

mat=[
    [11,12,13,14,15,16,17],
    [21,22,23,24,25,26,27],
    [31,32,33,34,35,36,37],
    [41,42,43,44,45,46,47]
]

n=4
m=7
minr=0
minc=0
maxr=n-1
maxc=m-1
count=0
t=n*m

while (count<t):
    #left
    i = minr
    j = minc
    while i <= maxr and count < t:
        print(mat[i][j],end=" ")
        i += 1
        count += 1
    minc += 1
    print()


    #bottom

    i=maxr
    j=minc
    while j<=maxc and count<t:
        print(mat[i][j],end=" ")
        j+=1
        count += 1
    maxr-=1
    print()

    #right
    i=maxr
    j=maxc
    while i>=minr and count<t:
        print(mat[i][j],end=" ")
        i-=1
        count += 1
    maxc-=1
    print()

    #top
    i=minr
    j=maxc
    while j>=minc and  count < t:

        print(mat[i][j],end=' ')
        j-=1
        count += 1
    minr+=1
    print()







































# mat=[
#     [11,12,13,14,15],
#     [21,22,23,24,25],
#     [31,32,33,34,35]
# ]
#
# n=3
# m=5
# minr=0
# minc=0
# maxr=n-1
# maxc=m-1
# t=n*m
# count=0
#
# while(count<t):
#     #left Wall
#     i=minr
#     j=minc
#     while i<=maxr and count<t:
#         print(mat[i][j],end=' ')
#         i+=1
#         count+=1
#     minc += 1
#     #bottomWall
#
#     i=maxr
#     j=minc
#     while j<=maxc and count<t:
#         print(mat[i][j],end=' ')
#         j+=1
#         count += 1
#
#     maxr -= 1
#
#     #rightWall
#     j=maxc
#     i=maxr
#     while i>=minr and count<t:
#         print(mat[i][j],end=' ')
#         i-=1
#         count += 1
#     maxc-=1
#
#
#     #topWall
#     i=minr
#     j=maxc
#     while j>=minc and count<t:
#         print(mat[i][j],end=" ")
#         j-=1
#         count += 1
#     minr+=1
#
#


