
def ReversePint(n):
    if n>0:


        print(n,end="")
        ReversePint(n-1)

        print(n,end="")

n=4



def Fact(n):
    if n>0:
        return (n * Fact(n-1))
    else:
        return 1

print(Fact(n))