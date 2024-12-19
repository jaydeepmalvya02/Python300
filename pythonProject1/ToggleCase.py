s="pepCODinG"
ans=''
for i in range(len(s)):
    c=s[i]
    if c>='a' and c<='z':
        ans+=chr(ord('A')+ord(c)-ord('a'))
    else:
        ans += chr(ord('a') + ord(c) - ord('A'))
print(ans)
a=(ord('A')+ord('p')-ord('a'))
print((a))