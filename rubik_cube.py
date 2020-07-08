def rotate(mat,n):
    for x in range(int(n/2)):
        for y in range(x,n-x-1):
            temp=mat[x][y]
            mat[x][y]=mat[y][n-1-x]
            mat[y][n-x-1]=mat[n-1-x][n-1-y]
            mat[n-1-x][n-1-y]=mat[n-1-y][x]
            mat[n-1-y][x]=temp
    return mat
n,k=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
while(k>0):
    mat=rotate(mat,n)
    k-=1
for i in range(n):
    print(*mat[i])
