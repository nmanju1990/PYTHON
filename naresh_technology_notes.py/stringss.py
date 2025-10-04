#Strings
#Operations on Strings
#Creation
#Empty String
'''
a1 = ""
a2 = ''
print(a1)
print(type(a1))
print(a2)
print(type(a2))
'''
#Single element
'''
a1 = "a"
a2 = 'a'
print(a1)
print(type(a1))
print(a2)
print(type(a2))
'''    
#Multiple elements
'''
a1 = "hello world"
a2 = 'hello world'
print(a1)
print(a2)
print(type(a1))
print(type(a2))
'''
#User inputs
'''
a1 = input("Enter String: ")
print(a1)
print(type(a1))
'''
#Accessing
#Indexing [ Accesing a single character from a string ]
#Positive Indexing
'''
b = "abcd"
print(b[2])
print(b[0])
'''
#Negative Indexing
'''
b = "abcd"
print(b[-2])
print(b[-1])
'''
#Looping [ Helps to access multiple values at a time ]
#With Range
'''
a = "python"
for i in range(6):
    print(i,a[i])
'''
#Example - 1
'''
Given a string.
Print the elements present in even Indexes.
python
p
t
o
nareshit
n
r
s
i
'''
#Source code:
'''
a = "nareshit"
n = 8
for i in range(n):
    if i%2==0:
        print(a[i])
'''
#Without Range
'''
a = "python"
for i in a:
    print(i)
'''
#Example - 2
'''
Given a string, find all the Vowels Present in the string.
education
e
u
a
i
o
'''
#Source Code:
#Approach - 1 [Without Range]
'''
a = "education"
for i in a:
    if i in "aeiou":
        print(i)
'''
#Approach - 2 [ With Range ]
'''
a = "education"
n = 9
for i in range(n):
    if a[i] in "aeiou":
        print(a[i])
'''
#Slicing
#Positive Slicing
'''
x = "pythonprogramming"
print(x[:])
print(x[::])
print(x[::1])
print(x[0::1])
print(x[0:17:1])
print(x[3:])
print(x[:5])
print(x[3:7])
print(x[2:10])
print(x[::3])
print(x[2:10:2])
'''
#Negative Slicing
'''
x = "abcd"
print(x[::1])
print(x[::-1])
'''
#Example - 4
'''
Given a String Print all the values present at odd indexes
pythonprogramming
yhnrgamn
'''
#Source Code
#Approach - 1
'''
a = "pyhtonprogramming"
for i in range(17):
    if i%2!=0:
        print(a[i],end="")
'''
#Approach - 2
'''
a = "pythonprogramming"
print(a[1::2])
'''














        
































