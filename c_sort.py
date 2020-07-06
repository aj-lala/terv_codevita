n=int(input())
l=[[int(i) for i in input().split()] for _ in range(n)]
l=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
for i in l:
    i.sort()
l=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
for i in l:
    print(*i)
