month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
y=[]
for m in range(1,13):
    for d in range(1,month[m]+1):
        y.append(((6-m)**2)+abs(d-15))
n=int(input())
r1,r2=map(int,input().split())
rev=int(input())
total=0
i=1
while(i<=n):
    t_total=0
    for p in y:
        if(p>n):
            p=n
        if(p>=(n-i)):
            ntv=(n-i)
            tv=p-ntv
        else:
            ntv=p
        t_total+=((tv*r1)+(ntv*r2))
    total=max(total,t_total)
    if(total>rev):
        break
    i+=1
print(min(i,n))
