x=2
n=5
def PowerLinear(x,n):
    if n>0:
        return (x)*PowerLinear(x,n-1)
    else:
        return 1

print(PowerLinear(x,n))


#ppower logarithm'

def PowerLog(x,n):
    if n>0:
        xpn=PowerLog(x,n//2)
        if n%2==0:
            return(xpn*xpn)
        else:
            return (xpn*xpn*x)
    else:
        return 1

print(PowerLog(x,n))