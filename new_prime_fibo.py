from itertools import permutations
import math
def prime(n):
    if(n==2 or n==3 or n==5):
        return True
    if(n<=1 or n%2==0):
        return False
    for i in range(3,math.ceil(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True
n1,n2=map(int,input().split())
l=[str(i) for i in range(n1,n2+1) if(prime(i))]
l=list(permutations(l,2))
l=list(set([int(''.join(list(i))) for i in l]))
nl=[i for i in l if(prime(i))]
a,b=min(nl),max(nl)
i=2
while(i<len(nl)):
    c=a+b
    a=b
    b=c
    i+=1
print(b)
