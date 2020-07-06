n=int(input())
l=[int(i) for i in input().split()]
lst=[bin(i)[2:].count('1') for i in l]
cnt=0
for i in range(n-1):
    for j in range(i,n):
        if(lst[i]>lst[j]):
            cnt+=1
print(cnt)
