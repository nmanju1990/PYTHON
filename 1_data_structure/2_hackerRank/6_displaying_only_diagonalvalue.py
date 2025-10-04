m = int(input("Enter No of Rows: "))
n = int(input("Enter No of Columns: "))
mat = []
for i in range(m):
    k = list(map(int,input().split()))
    mat.append(k)
for i in range(m):
    for j in range(m):
        if i==j:
            print(f"{mat[i][j]}",end=" ")
        else:
            print(" ",end=" ")
    print()  