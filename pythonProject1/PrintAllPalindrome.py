# s='abcc'
#
# n=len(s)
# for i in range(n):
#     j=i
#     p=''
#     k=i
#     while k<n:
#         while j<k+1:
#             p+=s[k]
#             j += 1
#             #print(p)
#             start = 0
#             end = len(p) - 1
#             while start <= end:
#                 if p[start] == p[end]:
#                     start += 1
#                     end -= 1
#                 else:
#                     break
#                 print(p)
#         k+=1
#
#
#

def PrintPalindrome(s,n):
    for i in range(n):
        for j in range(i+1,n+1):
            st=s[i:j]
            if isPalindrome(st):
                print(st)

def isPalindrome(st):
    low=0
    high=len(st)-1
    while low<high:
        if st[low]!=st[high]:
            return False
        low+=1
        high-=1
    return True


s='abcc'
n=len(s)
PrintPalindrome(s,n)