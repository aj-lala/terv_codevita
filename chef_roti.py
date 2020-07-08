import math
n=int(input())
l=list(map(int,input().split()))
sq=math.sqrt(2)-1
for s in l:
    s=(s/2)*sq
    print(math.floor(s**2),end=' ')
