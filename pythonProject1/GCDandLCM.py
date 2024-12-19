
#GCD
n1=int(input("First No"))
n2=int(input("second No"))
def GCD(n1,n2):
    div = n1
    dvd = n2
    while dvd % div != 0:
        rem = dvd % div
        dvd = div
        div = rem
    gcd = div
    return gcd

#LCM

def LCM(n1,n2):
    Lcm=(n1*n2)//GCD(n1,n2)
    return (Lcm)

LCM(n1,n2)
t=GCD(n1,n2)*LCM(n1, n2)
print(t)
print(n1*n2)
