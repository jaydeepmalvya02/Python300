n=int(input('Enter Len of Array: '))
arr=list(map(int,input().split()))
k=int(input('Enter the time pf rotatae: '))
k=k%n


if k<0:
    k=k+n
i=0
while i<k:
    temp = arr[-1]
    arr.insert(0,temp)
    arr.pop(n)
    i+=1
print(arr)