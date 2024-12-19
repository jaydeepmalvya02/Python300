b=int(input('base'))
n1=int(input('enter the to be subs ->'))
n2=int(input('Enter no from ->'))

def AnyBaseSub(b,n1,n2):
    pow=1
    ans=0
    carry=0
    while n1>0 and n2>0:
        d1=n1%10
        d2=n2%10-carry
        if d2-d1<0:
            d2+=b
            carry=1

        total=d2-d1


        ans+=total*pow
        pow*=10
        n1 = n1 // 10
        n2 = n2 // 10
    print(ans)

AnyBaseSub(b,n1, n2)


