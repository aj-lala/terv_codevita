fl=['F','L','A','M','E','S']
a=list(input().lower().replace(' ',''))
b=list(input().lower().replace(' ',''))
n=len(b)
for i in a:
    if(i in b):
        b.remove(i)
le=(len(a)-(n-len(b)))+len(b)
while(len(fl)>1):
    m=le%len(fl)
    fl=fl[m-1:]+fl[:m-1]
    fl.remove(fl[0])
print(fl[0])
