s='abecd'
n=len(s)
def Diff(s,n):
    ans=''
    for i in range(0,n-1):
        d=ord(s[i+1])-ord(s[i])
        ans+=s[i]+str(d)
        if i==n-2:
            ans+=s[n-1]
    print(ans)

Diff(s,n)