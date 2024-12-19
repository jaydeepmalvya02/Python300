n=int(input("Enter No:"))
div=2
while  div<=n:
    while n%div==0:
        print(div)
        n=n//div
    div += 1
