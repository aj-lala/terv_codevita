n,x=map(int,input().split())
l=list(map(int,input().split()))
rooms=0
s=''
for i in l:
    temp=0
    for j in range(1,i+1):
        rooms+=1
        if(rooms%x==0):
            temp+=1
    s+=str(temp%10)
print(s)
