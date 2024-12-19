
n=int(input("Enter Digit: "))
d=int(input("enter Target: "))
count=0
while n>0:
    digit=n%10
    if digit==d:
        count+=1
    n=n//10

print(count)





