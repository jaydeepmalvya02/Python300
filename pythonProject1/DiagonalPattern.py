n=14


for i in range(1,n):
    for j in range(1,n):
        if j==n-1  or j==1  or j==n-i or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()





#hourglass

# for i in range(1,n):
#     for j in range(1,n):
#         if i==n-1  or i==1  or j==n-i or i+1==j+1:
#             print('*',end=' ')
#
#
#         else:
#             print(' ',end=' ')
#     print()