n=int(input())
s,i=0,5
while(n//i>=1):
    s+=n//i
    i*=5
print(s)
