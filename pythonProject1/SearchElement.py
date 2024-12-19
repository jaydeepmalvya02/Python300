def SearchElement(a,data):
    for i in range(n):
        if a[i]==data:
            return i



n=int(input("enter Len :"))
a=list(map(int,input("Enter Element: ").split()))
data=int(input("Element to be Searched :"))

print(SearchElement(a,data))