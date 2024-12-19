arr=[0,0,1,2,2]
n=len(arr)
k=2

#using iteration
# def FirstLast(arr,n,k):
#     first=0
#     second=0
#     count=0
#     for i in range(1,n):
#         if arr[i]==k:
#             count+=1
#             if count==1:
#                 first=i
#             j=i+1
#             while arr[j]==k:
#                 j+=1
#             second=j-1
# #
# #
#     print(first,second)

# FirstLast(arr,n,k)

#using BinarySearch

def First(arr,n,k):
    fi=-1
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==k:
            fi=mid
            end=mid-1
        elif arr[mid]<k:
            start=mid+1
        else:
            end=mid-1
    return fi

def Second(arr,n,k):
    second=-1
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==k:
            second=mid
            start=mid+1
        elif arr[mid]<k:
            start=mid+1
        else:
            end=mid-1
    return second
f=First(arr,n,k)
s=Second(arr,n,k)

print(f,s)
