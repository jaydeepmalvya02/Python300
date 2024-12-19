arr=[5,10,15,22,33,40,42,55]
n=len(arr)
k=int(input("Enter Price->"))

def BrokenEco(arr,n,k):
    start=0
    end=n-1
    mid=(start+end)//2
    floor=-1
    ceil=-1
    while start<=end:
        if arr[mid]==k:
            return arr[mid]
        elif k<arr[mid]:
            end=mid-1
            ceil = arr[mid]

            mid=(start+end)//2

        else:
            start=mid+1
            floor = arr[mid]
            mid = (start + end) // 2
    return floor,ceil

b=BrokenEco(arr,n,k)

print(b)
