#Problem - 1 [ Find Duplicate Element ( V judge ) ]
'''
n = int(input())
x = tuple(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if x[i] == x[j]:
            print(x[i])
            break
'''
#Problem - 2 [ Find Unique Elements ( v judge ) ]
'''
n = int(input())
x = tuple(map(int,input().split()))
for k in x:
    if x.count(k) == 1:
        print(k,end=" ")
'''
#Problem - 3 [ Solve the Case ( V judge ) ] [ Tuple ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = tuple(map(int,input().split()))
    res = ()
    for i in x:
        if i not in res: # Memebership
            res = res + (i,) # Concatenation
    print(*res)
'''
#Problem - 4 [ Counting Pretty Numbers ( Code chef ) ]
#Approach - 1 [ Witout using Tuple ]
'''
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    res = 0
    for j in range(a,b+1):
        if j%10 == 2 or j%10 ==3 or j%10 == 9:
            res = res + 1
    print(res)
'''
#Approach - 2 [ Using Tuple ]
'''
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    pn = (2,3,9) # Tuple
    res = 0
    for j in range(a,b+1):
        if j%10 in pn: # Membership operators
            res = res + 1
    print(res)
'''
#Problem - 5 [ First Largest and Second Largest  (code chef ) ]
#Appraoch - 1 [ List ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split())) #List
    res = [] #Empty List
    for j in x:
        if j not in res:
            res.append(j) #append()
    res.sort() #Sort() -> Method
    print(res[-1] + res[-2])
'''
#Approach - 2 [ Tuples ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = tuple(map(int,input().split())) #Tuple
    res = () #Empty Tuple
    for j in x:
        if j not in res:
            res = res + (j,) #Concatenation
    r = sorted(res) #Built in Function
    print(r[-1] + r[-2])
'''















