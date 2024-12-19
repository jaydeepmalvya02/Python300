b=int(input("Base:"))
n1=int(input("initial no:"))
n2=int(input('Added to->'))
ans=0
carry=0
pow=1
while n1>0 and n2>0 or carry>0:
    d1=n1%10
    d2=n2%10
    t=d1+d2+carry

    carry=t//b

    rem=t%b

    ans+=rem*pow
    n1=n1//10
    n2=n2//10
    pow*=10

print(ans)



