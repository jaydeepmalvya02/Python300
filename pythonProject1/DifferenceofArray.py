n1=int(input('n1:'))
arr1=[]
for i in range(n1):
    vl=int(input())
    arr1.append(vl)
n2=int(input('n2:' ))
arr2=[]
for i in range(n2):
    vl=int(input())
    arr2.append(vl)
max=0
if n1>n2:
    max=n1
else:
    max=n2

result=[]*max

i=n1-1
j=n2-1
k=max-1
carry=0
while i>=0 or j>=0:
    d=0
    if carry==0:
        d=arr2[j]
    else:
        d=arr2[j]-1
    carry=0
    if i>=0:
        d-=arr1[i]
    if d<0:
        c=1
        d+=10
    result[k]=d
    i-=1
    j-=1
    k-=1
startzero=True
for i in range(max):
    if result[i]!=0:
        startzero=False
    if startzero==False:
        print(result[i])
