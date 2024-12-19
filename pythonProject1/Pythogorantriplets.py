a,b,c=map(int,input("Enter No").split())

if (a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a):
    print("true")
else:
    print("False")