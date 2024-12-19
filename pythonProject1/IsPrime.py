low=int(input("enter a no:"))
high=int(input("enter a no:"))


for n in range(low,high+1):
    count = 0
    i=2
    while i*i<=n:
        if n%i==0:
            count+=1
            break
        i+=1
    if count==0:
        print(n)



# def isPrime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return True
#     pass
#
# n=int(input("Enter the range"))
# if isPrime(n):
#     print("Prime")
#
# else:
#     print("Not Prime")
