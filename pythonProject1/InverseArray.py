arr=[4,0,2,3,1]
n=len(arr)
ans=[0]*n
i=0

while i<n:
    if arr[i]!=i:
        index=arr[i]
        ans[index]=i
    else:
        ans[i]=i
    i+=1
print(ans[:n])