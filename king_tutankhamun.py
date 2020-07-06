n=int(input())
l=[3,4]
for i in range(n//2):
    l.append(l[i]*10+3)
    l.append(l[i]*10+4)
print(l[n-1])
