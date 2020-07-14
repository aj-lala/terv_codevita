def prime(n):
    if(n>1):
        for i in range(2,n//2+1):
            if(n%i==0):
                return False
        return True
    return False
def digitsum(n):
    while(len(n)>1):
        n=[int(i)**2 for i in n]
        n=str(sum(n))
    return n
ul,ll,n=int(input()),int(input()),int(input())
l=[]
for i in range(ul,ll+1):
    x=digitsum(str(i))
    if((x=='1') and prime(i)):
        l.append(i)
if(len(l)>=n):
    print(l[n-1])
else:
    print('No number is present at this index')
