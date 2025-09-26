m = int(input("Enter Total Number of Rows: "))
n = int(input("Enter Total Number of Columns: "))
mat = []
#for i in range(m):
#    x = list(map(int,input().split()))
#    mat.append(x)
#print(mat)
print("1. ---------------------------------------------")

for i in range(m):
    x = list(map(int, input().split()))
    if len(x) != n:
        print(f"Error: Row {i+1} must have exactly {n} columns!")
        exit()
    mat.append(x)
print(mat)

#mat = [[10,20,30],[40,50,60],[70,80,90]]
print("2. Matrix/2d array traverse ---------------------------------------------")
for x in mat:
    print(*x)
