#Problem - 1 [ Sove the Case ( code chef ) ]
#Approach - 1 
'''
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    res = []
    for k in a:
        if k not in res:
            res.append(k)
    print(*res,sep=" ")
'''
#Appraoch - 2
'''
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    res = []
    for i in range(1,n):
        if a[i] != a[i-1]:
            res.append(a[i-1])
    res.append(a[-1])
    print(*res,sep=" ")
'''
#Problem - 2 [ Chef Team ( code chef ) ]
#Apporach - 1 [ without using list ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    t1=t2=0
    for k in range(1,n+1):
        if n%k==0:
            if k%2==0:
                t1 = t1 + 1
            else:
                t2 = t2 + 1
    if t1 == t2:
        print(1)
    else:
        print(0)
'''
#Approach - 2 [ Using List ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    factors = []
    for j in range(1,n+1):
        if n%j==0:
            factors.append(j)
    #print(factors)
    t1 = []
    t2 = []
    for k in factors:
        if k%2==0:
            t1.append(k)
        else:
            t2.append(k)
    #print(t1)
    #print(t2)
    if len(t1) == len(t2):
        print(1)
    else:
        print(0)
'''
#Approach - 3
'''
t = int(input())
for i in range(t):
    n = int(input())
    #List Comprehension
    factors = [j for j in range(1,n+1) if n%j==0]
    t1,t2=[],[]
    for k in factors:
        if k%2==0:
            t1.append(k)
        else:
            t2.append(k)
    #Conditional Expression
    print(1 if len(t1)==len(t2) else 0)
'''
#Problem - 3 [ Code chef Streak ( code chef ) ]
'''
t = int(input()) # input formatting
for i in range(t): # range() & looping
    n = int(input()) # input formatting
    om = list(map(int,input().split())) # input formatting
    addy = list(map(int,input().split())) # input formatting
    om_s = [] #Creation of Empty list
    addy_s = [] #Creation of Empty list
    a1 = 0 #Assignment
    a2 = 0 #Assignment
    for k in om: #For loop without range
        if k == 0: #Conditional Statements
            om_s.append(a1) #Insertion of element in list
            a1 = 0 #Assignment
        else: #Conditional Statements
            a1 = a1 + 1 #Add and Assignment operator
    om_s.append(a1) #Insertion of element in list
    for k in addy:
        if k == 0:
            addy_s.append(a2)
            a2 = 0
        else:
            a2 = a2 + 1
    addy_s.append(a2)
    m1 = max(om_s) #Builtin Functions of List
    m2 = max(addy_s) #Builtin Functions of List
    if m1 > m2:
        print("Om") #Ouput formatting
    elif m1 < m2:
        print("Addy")
    else:
        print("Draw")
'''
#Doubts
'''
@
@ @
@ @ @
@ @ @ @
'''
x = [["@"],["@","@"],["@","@","@"],["@","@","@","@"]]
'''
for k in x:
    print(*k)
'''
x = x[::-1]
for k in x:
    print(*k)

            



    
