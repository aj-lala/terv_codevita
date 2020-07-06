n,k=map(int,input().split())
l=[input().split() for i in range(n)]
b=[[None]*n for _ in range(n)]
le=n//2
x,rot=[],[]
for c in range(n//2):
    ix=[]
    for i in range(c,n-c):
        ix.append((c,i))
    for i in range(c+1,n-1-c):
        ix.append((i,n-1-c))
    for i in range(c,n-c)[::-1]:
        ix.append((n-1-c,i))
    for i in range(1+c,n-1-c)[::-1]:
        ix.append((i,c))
    if(not ix):
        break
    x.append(ix)
for i in x:
    val=k%len(i)
    rot.append(i[val:]+i[:val])
for (u,v) in zip(x,rot):
    for ((c,d),(e,f)) in zip(u,v):
        b[c][d]=l[e][f]
if(n%2!=0):
    b[le][le]=l[le][le]
for i in b:
    print(*i)
