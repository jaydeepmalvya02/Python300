n=int(input('enter no: '))
k=int(input('Enter time of rotation:'))
c=0
rem=0
temp=n
while n>0:
    d=n%10
    c+=1
    n=n//10
print(c)
rem=temp%(pow(10,k))
print(rem)
quo=temp//(pow(10,k))
print(quo)
mul=pow(10,c-k)
ans=rem*mul+quo
print(ans)
