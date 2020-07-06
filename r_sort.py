n=int(input())
l=[input().split() for i in range(n)]
for i in l:
    print(*sorted(i))
