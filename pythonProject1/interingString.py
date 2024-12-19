import sys
a=sys.intern('hello'*4097)
b=sys.intern('hello'*4097)
c="hello"
print(id(a))
print(id(b))
print(a is c) #it check memory address and instance which is different
print(a==b) # first check instance then check reference
