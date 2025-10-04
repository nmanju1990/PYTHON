#List Operations
#Insertion
#append()
#Examaple - 1
'''
a = [10,20,30,40]
print(a)
a.append(50)
print(a)
a.append(120)
print(a)
'''
#extend()
#Example - 2
'''
a = [10,20,30,40]
print(a)
a.extend([50,60,70])
print(a)
'''
#Diff b/w append() and Extend()
#EXample - 3
'''
a = [10,20,30]
b = [10,20,30]
print(a)
print(b)
a.append([40,50,60])
b.extend([40,50,60])
print(a)
print(b)
print(a[-1])
print(b[-1])
'''
#insert()
#Example - 4
'''
a = [10,20,30,40,50]
print(a)
a.insert(2,25)
print(a)
a.insert(0,5)
print(a)
'''
#Deletion
#pop
#Example - 5
'''
a = [10,20,30,40,50]
print(a)
a.pop()
print(a)
a.pop()
print(a)
b = []
b.pop()
'''
#Example - 6
'''
a = [10,20,30,40,50]
print(a)
a.pop(2)
print(a)
b = [10,20,30,40,20,50]
print(b)
b.pop(1)
print(b)
b.pop(10)
'''
#remove()
#Example - 7
'''
a = [10,20,30,40,50]
print(a)
a.remove(30)
print(a)
'''
#Example - 8
'''
a = [10,20,30,20,40,50]
print(a)
a.remove(20)
print(a)
'''
#EXample - 9
'''
a = [10,20,30]
print(a)
a.remove(100)
'''
#clear()
#Example - 10
'''
a = [10,20,30,40]
print(a)
a.clear()
print(a)
'''
#Example - 11
'''
a = []
print(a)
a.clear()
print(a)
'''
#Updation
#Indexing
#Example - 12
'''
a = [10,20,30,40,50]
print(a)
a[2] = 300
print(a)
a[-1] = "Hello"
print(a)
'''

#External Operations
#Concatenation
#Example - 13
'''
a = [10,20,30]
b = [40,50,60]
print(a+b)
'''
#Repeateation
#Example - 14
'''
a = [10,20,30]
print(a*3)
'''
#Membsership
#Example - 15
'''
a = [10,20,30,40]
print(10 in a)
print(10 not in a)
print(100 in a)
print(100 not in a)
'''

#Diff b/w extend() and concatenation
#Example - 16
'''
a = [10,20,30]
b = [40,50]
a.extend(b)
print(a)
'''
#Example - 17
'''
a = [10,20,30]
b = [40,50]
print(a+b)
'''
#Note: By using Extend we can not
#able to find the previous value
#of a variable
#Example - 18
'''
a = [10,20,30]
print(a)
a.extend([400,500])
print(a)
print(a)
'''
#Example - 19
'''
a = [10,20,30]
print(a)
print(a + [400,500])
print(a)
'''

#Built in functions
#Example - 20
'''
a = [10,20,30,40]
#min()
print(min(a))
#max()
print(max(a))
#Len()
print(len(a))
#sum()
print(sum(a))
'''

#Nested lists
'''
a = [[10,20],[30,40],[50,60]]
print(len(a))

print(a[0][1])
print(a[2][0])
print(a[-1][0])
print(a[-1][-1])
'''
#List Comprehension
#Program - 1
'''
Given an integer input, Find
the numbers from 1 to n and
store in a list
=> 5
=> [1,2,3,4,5]

=> 8
=> [1,2,3,4,5,6,7,8]
'''
#Source code:
#Approach - 1 [ Insertion Methods ]
'''
n = int(input())
temp = []
for i in range(1,n+1):
    temp.append(i)
print(temp)
'''
#Approach - 2 [ List Comprehension ]
'''
n = int(input())
temp = [i for i in range(1,n+1)]
print(temp)
'''
#Program - 2
'''
Given an integer input, find all
the even number from 1 to n and
store it in list.
'''
#Source Code
#Approach - 1 [ List Operations ]
'''
n = int(input())
temp = []
for i in range(1,n+1):
    if i%2==0:
        temp.append(i)
print(temp)
'''
#Appraoch - 2 [ List Comprehension]
'''
n = int(input())
temp = [i for i in range(1,n+1) if i%2==0]
print(temp)
'''

#Problem - 3 [ Volume control - Code chef]
#Approach - 1
'''
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x > y:
        print(x-y)
    else:
        print(y-x)
'''
#Approach - 2
'''
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(abs(x-y))
'''
#doubts
'''
a = [10,20,30,40]
print(a)
a.clear()
print(a)
'''
#Example
a = [10,20,30,40,50]
#Need of index values
'''
for i in range(5):
    print(a[i])
'''
#No Need of index values
'''
for i in a:
    print(i)
'''






