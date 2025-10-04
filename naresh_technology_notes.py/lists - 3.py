#Nested Lists [ Matrix ]
#Problem - 1 [ Taking values from the user ]
'''
m = int(input("Enter Total Number of Rows: "))
n = int(input("Enter Total Number of Columns: "))
mat = []
for i in range(m):
    x = list(map(int,input().split()))
    mat.append(x)
print(mat)
'''
#Problem - 2 [ Displaying Matrix Values ]
'''
mat = [[10,20,30],[40,50,60],[70,80,90]]
for x in mat:
    print(*x)
'''
#Problem - 3
'''
Take two matrices from the user
Print the sum of two matrices
'''
#Source Code
'''
m = int(input("Enter no of Rows: "))
n = int(input("Enter no of Columns: "))
print("Enter 1st Matrix values")
matrix1 = []
for i in range(m):
    x = list(map(int,input().split()))
    matrix1.append(x)
print("Enter 2nd Matrix Values")
matrix2 = []
for i in range(m):
    x = list(map(int,input().split()))
    matrix2.append(x)
print(matrix1)
print(matrix2)
res = []
for i in range(m):
    res.append([0]*n)
for i in range(m):
    for j in range(n):
        res[i][j] =  matrix1[i][j] + matrix2[i][j]
print(res)
'''
#Problem - 4
'''
Take two matrices from the user
Print the subtraction of two matrices
'''
#Source Code
'''
m = int(input("Enter no of Rows: "))
n = int(input("Enter no of Columns: "))
print("Enter 1st Matrix values")
matrix1 = []
for i in range(m):
    x = list(map(int,input().split()))
    matrix1.append(x)
print("Enter 2nd Matrix Values")
matrix2 = []
for i in range(m):
    x = list(map(int,input().split()))
    matrix2.append(x)
#print(matrix1)
#print(matrix2)
res = []
for i in range(m):
    res.append([0]*n)
for i in range(m):
    for j in range(n):
        res[i][j] =  matrix1[i][j] - matrix2[i][j]
for x in res:
    print(*x)
'''
#Problem - 4
'''
Take the value of the matrix and find the the left daignol sum
3
3
10 20 30
40 50 60
70 80 90
'''
#source code
'''
#Taking Matrix Values from the user
m = int(input())
m1 = []
for i in range(m):
    x = list(map(int,input().split()))
    m1.append(x)
#Operation
temp = 0
for i in range(m):
    for j in range(m):
        if i == j:
            temp = temp + m1[i][j]
print(temp)
'''
#Problem - 5
'''
Take the matrix from the user and create transpose of the matrix.
2
10 20
30 40

=> [[10,20],[30,40]]
=> Transpose : [[10,30],[20,40]]
'''
#Soruce Codes
'''
m = int(input("Enter No of Rows: "))
n = int(input("Enter No of Columns: "))
mat = []
for i in range(m):
    x = list(map(int,input().split()))
    mat.append(x)
res = []
for i in range(m):
    res.append([0]*n)
for i in range(m):
    for j in range(n):
        res[i][j] = mat[j][i]
print("The Transpose of the Matrix is: ")
for x in res:
    print(*x)
'''
#Problem - 6
'''
Take a matrix from the use, Print the structure of matrix by
displaying only diagnal values
3
10 20 30
40 50 60
70 80 90

10
   50
      90
'''
#Source code
'''
m = int(input("Enter Size of the matrix: "))
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
'''
#Assignment Questions
'''
1. Find Multiplication of two matrices
2. Find the product of right daignal values
1 2 3
4 5 6
7 8 9
=>3*5*7 => 105
'''
#Note: We can also solve pattern programs by using nested list
#Pattern - 1
'''
n = 5
@ @ @ @ @
@ @ @ @ @
@ @ @ @ @
@ @ @ @ @
@ @ @ @ @
'''
#Source code
'''
n = int(input())
res = []
for i in range(n):
    res.append(["@"]*n)
for x in res:
    print(*x)
'''
#Pattern - 2
'''
n = 5
@
@ @
@ @ @
@ @ @ @
@ @ @ @ @
'''
#Source code
'''
n = int(input())
res = []
for u in range(n):
    res.append(["@"]*(u+1))
for x in res:
    print(*x)
'''




















