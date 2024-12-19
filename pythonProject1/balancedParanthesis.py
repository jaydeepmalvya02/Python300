s="()[{}()]"

ans=[]
for i in s:
    if i=="(" or i=="[" or i=="{":
        ans.append(i)
    elif i==")" and ans[-1]=="(":
        ans.pop()
    elif i=="]" and ans[-1]=="[":
        ans.pop()
    elif i=="}" and ans[-1]=="{":
        ans.pop()

print(ans)