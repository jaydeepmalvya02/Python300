n=int(input("No to be Convert"))
a=int(input("from->"))
b=int(input('to->'))
def DecToAny(n,a,b):
    ans=0
    pow=1
    while n>0:
        digit=n%b
        ans+=digit*pow
        n=n//b
        pow*=a
    print(ans)

DecToAny(n,a,b)
