n=int(input("Enter No"))
b=int(input("->"))
def DecToAny(n,b):
    ans=0
    pow=1
    while n>0:
        digit=n%b
        ans+=digit*pow
        n=n//b
        pow*=10
    print(ans)

DecToAny(n,b)




def OcttoDec(n,b):
    ans=0
    pow=1
    while n>0:
        digit=n%10
        ans+=digit*pow
        n=n//b
        pow*=8
    print(ans)

OcttoDec(n,b)
