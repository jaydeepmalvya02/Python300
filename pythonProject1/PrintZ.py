def Z(rows):
    for i in range(1,rows+1):
        for j in range(1,rows+1):
            if i==1 or j==rows+1-i or i==rows:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


    pass
rows=int(input("enter Rows:"))
Z(rows)