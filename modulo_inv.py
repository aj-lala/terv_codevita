def modInverse(a,m):
    m0=m
    y=0
    x=1
    if(m==1):
        return 0
    while(a>1):
        q=a//m
        t=m
        m=a%m
        a=t
        t=y
        y=x-q*y
        x=t
    if(x<0): 
        x=x+m0 
    return x
for _ in range(int(input())):
    n,t,m=map(int,input().split())
    d=m/t
    if(isinstance(d,float)):
        print(m*modInverse(t,1000000007))
    else:
        print(d)

