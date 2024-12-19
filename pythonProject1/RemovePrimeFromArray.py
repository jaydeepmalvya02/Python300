arr=[20,10,3,4]
n=len(arr)

def Remove(arr,n):
    ans=[]
    for i in range(n):
        c=0
        for j in range(1,arr[i]):
            if arr[i]%j==0:
                c+=1
        if c>1:
            ans.append(arr[i])

    print(ans)

Remove(arr,n)