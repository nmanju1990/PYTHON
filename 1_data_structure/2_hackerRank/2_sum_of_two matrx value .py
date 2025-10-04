m=int(input("enter number of rows"))
n=int(input("enter number of columns"))
print("enter 1st matrix values")
matrix1=[]
for i in range(m):
    x=list(map(int,input().split())
           )
    matrix1.append(x)


print("enter 2nd matix values:")    
matrix2=[] 
for i in range(m):
    x=list(map(int,input().split())
           )
    matrix2.append(x)
print(matrix1)
print(matrix2)
res=[]
for i in range(m):
    res.append([0]*n
               )    
for i in range(m):
    for j in range(n):
        res[i][j]=matrix1[i][j] + matrix2[i][j]
print(res)      

           