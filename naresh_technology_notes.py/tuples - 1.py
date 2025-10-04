#Tuples
#Creation
#Create Empty Tuple
'''
t = ()
print(t)
print(type(t))
'''
#Create With Single element
'''
t = (10,)
print(t)
print(type(t))
a = ("Hello",)
print(a)
print(type(a))
'''
#Create with multiple Elements
'''
t1 = (10,20,30,40)
print(t1)
print(type(t1))
t2 = (10,"hello",3.14,True)
print(t2)
print(type(t2))
'''
#Create With User Inputs
'''
t1 = tuple(map(int,input().split()))
print(t1)
print(type(t1))

t2 = tuple(input().split())
print(t2)
print(type(t2))
'''

#Accessing
#Indexing -> To access single value at a time
#Positive Indexing
'''
a1 = (10,20,30,40,50)
print(a1[0])
print(a1[3])
'''
#Negative Indexing
'''
a1 = ("hello","python","program")
print(a1)
print(a1[-1])
print(a1[-3])
'''
#Looping -> To access all elements at a time
#For Loop with range
'''
a = (10,50,30,21)
for i in range(4):
    print(i,a[i])
'''
#For Loop with out range
'''
a = (10,50,30,21)
for i in a:
    print(i)
'''
#Slicing -> To access multiple elements
'''
a = (10,20,30,40,50,60,70,80)
print(a[:])
print(a[::])
print(a[0::1])
print(a[::2])
print(a[1::2])
print(a[2:6])
print(a[2:6:2])
print(a[::-1])
'''
#Methods
'''
a = (10,20,30,40)
print(a.index(30))
print(a.index(20))
'''
#Example [ Performing some intersion operation ]
'''
a = (10,20,30,40)
print(a)
a.append(50)
print(a)
'''
#External Operations
#Concatenation [ + ]
'''
a = (10,20,30)
print(a)
b = (40,50,60)
print(b)
print(a+b)
print(b+a)
'''
#Repeatetion [ * ]
'''
a = (10,20)
print(a)
print(a*1)
print(a*2)
print(a*3)
'''
#Membership [ in | not in ]
'''
a = (100,200,300,400)
print(100 in a)
print(1000 in a)
print(1000 not in a)
print(100 not in a)
'''
#Built in Functions
'''
a = (3,2,5,4,3)
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(sorted(a))
'''


#copy()
#Example - 1
'''
a = [10,20,30,40]
a1 = a #Deep Copy
print(a1)
a2 = a.copy() #Shallow Copy
print(a2)
'''
#Example - 2 [ Shallow Copy -> copy() ]
'''
a1 = [10,20,30,40]
a2 = a1.copy() #Shallow
print(a1)
print(a2)
a1[0] = 100
print(a1)
print(a2)
a2[-1] = 400
print(a1)
print(a2)
'''
#Example - 3 [ Deep Copy -> = ]
'''
a1 = [10,20,30,40]
a2 = a1 #Deep
print(a1)
print(a2)
a1[0] = 100
print(a1)
print(a2)
a2[-1] = 400
print(a1)
print(a2)
'''
#Problem - [ Prefix Sum ( Code Chef ) ]
#Approach - 1 [ Looping ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = tuple(map(int,input().split()))
    q = int(input())
    for j in range(q):
        a,b = map(int,input().split())
        temp = 0
        for k in range(a-1,b): #Looping
            temp = temp + x[k]
        print(temp)
'''
#Approach - 2 [ Slicing ]
'''
t = int(input())
for i in range(t):
    n = int(input())
    x = tuple(map(int,input().split()))
    q = int(input())
    for k in range(q):
        a,b = map(int,input().split())
        print(sum(x[a-1:b])) #Slicing
'''
#Lists Problems
'''
Given n vlaue
Store and print all the vlaues from 1 to n in an list
'''
#Approach - 1
'''
n = int(input())
x = []
for i in range(1,n+1):
    x.append(i)
print(x)
'''
#Approach - 2
#Ouput Expression - [ i ]
#Input Sequence - [ for i in range(1,n+1) ]
#condition - [ No condition ]
#Syntax:
    # x = [output expression Input sequence condition]
'''
n = int(input())
x = [i for i in range(1,n+1)]
print(x)
'''




































