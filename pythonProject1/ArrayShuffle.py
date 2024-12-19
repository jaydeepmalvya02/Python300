a=[1,2,3,4,5,6,7,8,9,10]

mid=len(a)//2
end=len(a)
for i in range(1,end,2):
    a.insert(i,a[mid])
    a.pop(a[mid+1])
    mid=mid+1
    end-=1

print(*a)



