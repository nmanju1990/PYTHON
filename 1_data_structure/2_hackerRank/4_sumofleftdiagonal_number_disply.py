m=int(input("enter number of rows"))
n=int(input("enter number of columns"))
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