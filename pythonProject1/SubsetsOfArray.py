

def DecToBin(d,l):
    list1=[]

    while l>0:
        t=d%2
        d=d//2
        list1.insert(0,t)
        l-=1
    return list1


arr=[10,20,30,40,50,60]
n=len(arr)
def SubSets(arr,n):

    ts=2**n
    for i in range(0,ts):
        list1=DecToBin(i,n)
        for j in range(0,n):
            if list1[j]==0:
                print('-','\t',end='')
            else:
                print(arr[j],'\t',end='')
        print()
SubSets(arr,n)

