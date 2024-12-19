s='wwwaabccaassddd'
n=len(s)

def StringComp(s,n):
    c1=''
    c2=''
    i=0
    while i<n-1:

        for j in range(i+1,n):
            c = 1
            if s[i]!=s[j]:
                c1+=s[i]
                print(s[i],end=' ')
                i+=1
            if j==n-1:
                c1+=s[i]
                c2+=s[i]
            else:
                c+=1


        if c>1:
            print(c)
        i += 1

    print(c1,c2,end=" ")

StringComp(s,n)