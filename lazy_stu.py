import math
def fact(n):
    s=1
    for i in range(2,n+1):
        s*=i
    return s
for _ in range(int(input())):
    n,t,m=map(int,input().split())
    a,b,c=fact(n-m),fact(t),fact(n-m-t)
    x=1-((a)/(a*b))
    p,q=x.as_integer_ratio()
    mod=1000000007
    print(pow(q,mod-2,mod))
    
