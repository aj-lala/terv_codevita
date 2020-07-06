n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=1
for i in l:
    if(ans>=i):
        ans+=i
    else:
        break
print(ans)
