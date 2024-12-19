b=int(input('Base->'))
n1=int(input('First No->'))
n2=int(input('second No->'))

def AnyBaseMul(b,n1,n2):
    ans=0
    p=1
    while n2>0:

        d2=n2 % 10
        n2=n2//10
        pwod=getProductSingle(b,n1,d2)
        ans=GetSum(b,ans,pwod*p)
        p*=10
    return ans
def getProductSingle(b,n1,d2):
    carry = 0
    total = 0
    p=1
    while n1 > 0 or carry > 0:
        d1 = n1 % 10
        t = d1 * d2 + carry
        carry = t // b
        rem = t % b
        total += rem * p

        n1 = n1 // 10
        p*= 10

    return total








def GetSum(b,n1,n2):
    ans = 0
    carry = 0
    p = 1
    while n2 > 0 :
        d1 = n1 % 10
        d2 = n2 % 10
        t = d1 + d2 + carry

        carry = t // b

        rem = t % b

        ans += rem * p
        n1 = n1 // 10
        n2 = n2 // 10
        p *= 10
    return ans

print(AnyBaseMul(b,n1,n2))