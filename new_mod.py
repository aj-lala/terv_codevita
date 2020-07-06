import math
from itertools import combinations
def mulInverse(n):
    mo=1000000007
    i=1
    b=1
    while(i<m):
        if((i*m+1)%n==0):
            b=(i*m+1)/n
            break
    return b
def comb(n,m):
    l=[1]*n
    return len(list(combinations(l,m)))
    #return(fact(n)/(fact(m)*fact(n-m)))
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
def _gcd(a,b):
  return a if(b==0) else _gcd(b,a%b)
for _ in range(int(input())):
    n,t,m=list(map(int,input().split()))
    u=n-t
    c=comb(n,m)
    f=comb(u,m)
    x=c-f
    g=_gcd(x,c)
    if(g!=1):
        x//=g
        c/=g
    r=(x*mulInverse(c))%1000000007
    print(r)
