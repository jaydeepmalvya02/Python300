arr=['a','b','c','d','e']
n=len(arr)
i=0
while i<n:
    j=i
    while j<n:
        k=i
        while k<j+1:
            print(arr[k],end=" ")
            k+=1
        print()
        j += 1
    i+=1

