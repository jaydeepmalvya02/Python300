arr=[3,4,6,7,9,13,17,26,34,37,50]
n=len(arr)
k=int(input("Enter no to be search"))
def BinarySearch(arr,n,k):
    start=0
    end=n-1
    mid=(start+end)//2
    while start<=end:
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            start=mid+1
            mid=(start+end)//2

        else:
            end=mid-1
            mid=(start+end)//2
    return -1

print(BinarySearch(arr,n,k))