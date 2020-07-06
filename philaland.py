for _ in range(int(input())):
    n=int(input())
    cnt=0
    while(n>=1):
        n//=2
        cnt+=1
    print(cnt)
