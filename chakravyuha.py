s=int(input())
n=m=s
a=[[0 for j in range(n)] for i in range(n)]
c={0:(0,0)}
val,k,l=1,0,0
while(k<m and l<n):
    for i in range(l,n):
        a[k][i]=val
        val+=1
    k+=1
    for i in range(k,m):
        a[i][n-1]=val
        val+=1
    n-=1
    if(k<m):
        for i in range(n-1,l-1,-1):
            a[m-1][i]=val
            val+=1
        m-=1
    if(l<n):
        for i in range(m-1,k-1,-1):
            a[i][l]=val
            val+=1
        l+=1
for i in range(s):
    for j in range(s):
        print(a[i][j],end='\t')
        if(a[i][j]%11==0):
            c[a[i][j]//11]=[i,j]
    print()
print(len(c))
for i in range(len(c)):
    print('({},{})'.format(c[i][0],c[i][1]))
