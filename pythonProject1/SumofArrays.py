
# arr1=[1,2,3,4,5]
# n1=len(arr1)
#  for i in range(n1):
#      val1=int(input())
#      arr1.append(val1)
#
#
# arr2=[6,7,8,9,10]
# n2=len(arr2)
#  for i in range(n1):
#      val2=int(input())
#      arr2.append(val2)
#
# k=max(n1,n2)
# result=[]
# for i in range(k):
#     result.append(0)
# i=n1-1
# j=n2-1

# carry=0
#
# while k>0:
#     d=carry
#     if i>=0:
#         d+=arr1[i]
#     if j>=0:
#         d+=arr2[j]
#     carry=d//10
#     d=d%10
#     result[k-1]+=d
#     i-=1
#     j-=1

#     k-=1
# if carry>0:
#     print(carry)
# for x in result:
#     print(x)

















arr1=[1,2,3,4,5,6,7]
n1=len(arr1)
arr2=[3,4,5,6,7]
n2=len(arr2)
k=max(n1,n2)

result=[]
for i in range(k):
    result.append(0)
i=n1-1
j=n2-1

carry=0
while k>=0:
    d=carry
    if i>=0:
        d+=arr1[i]
    if j>=0:
        d+=arr2[j]
    carry=d//10
    d=d%10
    result[k-1]+=d

    i-=1
    j-=1
    k-=1
if carry>0:
    print(carry)
for i in result:
    print(i)
