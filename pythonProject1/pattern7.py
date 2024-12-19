
n=int(input("Enter range"))

def Pattern1(n):
    for i in range(n):
        for j in range(n):
            if (j==i) or  j==n-i-1:
                print("*",end="\t")
            else:
                print("",end="\t")
        print()





def Pattern2(n):
    otsp = n // 2
    insp = -1
    for i in range(n):

        for j in range(otsp):

            print("",end="\t")
        print("*\t",end="")



        for k in range(insp):
            print("", end="\t")
        if i!=0 and i!=n-1:

            print("*\t",end='')



        if i<n//2:
            otsp-=1
            insp+=2
        else:
            otsp+=1
            insp-=2
        print()

def Pattern3(n):
    p=1
    for i in range(n):
        for j in range(i+1):
            print(p,end="\t")
            p+=1
        print()



def Pattern4(n):
    a = 0
    b = 1

    for i in range(1,n+1):


        for j in range(1,i+1):
            print(a,end="\t")
            c = a + b
            a = b
            b = c

        print()

def Pattern5(n):
    i=0
    while i<n:
        a=1
        j=0
        while j<=i:
            print(a,end="\t")
            b=(a*(i-j)//(j+1))
            a=b
            j+=1
        print()
        i+=1

def Pattern14(n):
    x=n
    i=1
    while i<11:
        print(x,'* ', i, '= ', x*i, end='\t')
        i+=1
        print()



def Pattern15(n):
    sp=n//2
    np=1
    p=1
    for i in range(n):
        for j in range(sp):
            print('',end='\t')
        for k in range(1,np+1):
            print(p,end='\t')
            if k<=np//2:
                p+=1
            else:
                p-=1



        if i<n//2:
            p+=1
            sp-=1
            np+=2
        else:
            sp+=1
            np-=2
            p-=1
        print()
        p+=1

def Pattern16(n):
    sp = 2 * n - 3
    st = 1
    for i in range(1,n+1):

        for j in range(st):
            print(j+1,end='\t')
        for s in range(sp):
            print('-',end='\t')
        if i==n:
            st-=1
        p=st
        while p>=1:
            print(p,end='\t')
            p-=1
        print()

        st+=1
        sp-=2

Pattern16(n)