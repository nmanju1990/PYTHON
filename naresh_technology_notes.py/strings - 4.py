#Problem - 1 [ Decode String ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = input()
    x = x[::-1] 
    alpha = "abcdefghijklmnopqrstuvwxyz"
    temp = 0
    res = ""
    while temp != n:
        if x[temp] != '0':
            res = res + alpha[int(x[temp])-1]
            temp = temp + 1
        else:
            t1 = x[temp+1] + x[temp+2]
            t1 = int(t1[::-1])
            res = res + alpha[t1-1]
            temp = temp + 3
    res = res[::-1]
    print(res)
'''
#Problem - 2 [ Love Story ]
'''
t = int(input())
const = "codeforces"
for i in range(t):
    s = input()
    temp = 0
    for j in range(10):
        if const[j] != s[j]:
            temp = temp + 1
    print(temp)
'''
#Problem - 3 [ Guess the Output - 1 ]
'''
t = int(input())
for i in range(t):
    a,b = input().split()
    res = ""
    for j in b:
        if j not in a:
            res = res + j
    print(res)
'''





















        
        
