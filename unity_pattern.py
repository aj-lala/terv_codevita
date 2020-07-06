n=int(input())
for i in range(1,n+1):
    x=n
    for j in range(1,i):
        print(x,end=' ')
        x-=1
    for j in range(1,(2*n)-(2*i)+2):
        print(n-i+1,end=' ')
    for j in range(1,i):
        x+=1
        print(x,end=' ')
    print()
for i in range(n-1,0,-1):
    x=n
    for j in range(1,i):
        print(x,end=' ')
        x-=1
    for j in range(1,(2*n)-(2*i)+2):
        print(n-i+1,end=' ')
    for j in range(1,i):
        x+=1
        print(x,end=' ')
    print()
