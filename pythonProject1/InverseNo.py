n=int(input('Enter a number: '))

op=1
inv=0
while n>0:
    od=n%10
    np=od
    nd=op
    mul=pow(10,np-1)
    inv+=nd*mul
    op+=1
    n=n//10
print(inv)

