n=int(input('no to be convert:'))
a=int(input('from->'))
b=int(input('To->'))
def AnyToAny(n,a,b):
    temp=AnyToDec(n,a)
    ans=DecToAny(temp,b)
    print(ans)
def AnyToDec(n,b):
    ans=0
    pow=1
    while n>0:
        digit=n%a
        ans+=digit*pow
        n=n//a
        pow*=a
    return ans


def DecToAny(temp,b):
    ans=0
    pow=1
    while temp>0:
        digit=temp%b
        ans+=digit*pow
        temp=temp//b
        pow*=10
    return ans


AnyToAny(n,a,b)