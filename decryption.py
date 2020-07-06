s=input()[::-1]
x=''
for i in range(0,len(s),2):
    x=s[i]+x
    x=x*int(s[i+1])
print(x)
