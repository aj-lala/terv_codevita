def gcd(a,b):
    return a if(b==0) else gcd(b,a%b)
n=int(input())
l=[[int (i) for i in input().split()] for _ in range(n)]
x=[l[i][i] for i in range(n)]
res=x[0]
for i in range(1,n-1):
    res=gcd(res,x[i])
print(res)
