from itertools import permutations
import math
def prime(n):
    if(n==2):
        return True
    elif(n==1 or n&1==0):
        return False
    for i in range(3,math.ceil(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True
n1,n2=list(map(int,input().split()))
l=[]
for i in range(n1,n2+1):
    if(prime(i)):
        l.append(str(i))
l=list(permutations(l,2))
l=list(set([int(''.join(list(i))) for i in l]))
nl=[]
for i in l:
    if(prime(i)):
        nl.append(i)
a,b,le=min(nl),max(nl),len(nl)
x=[a,b]
for i in range(le-1):
    x.append(x[-1]+x[-2])
print(x[le-1])
