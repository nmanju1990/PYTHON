#Dictionary
#Creation
#Empty Dictionary
'''
x = {}
print(x)
print(type(x))
'''
#Single Element
'''
s = {10:100}
print(s)
print(type(s))
s2 = {10:45.67}
print(s2)
print(type(s2))
'''
#Multiple Elements
'''
x = {10:100,20:45.67,30:"Hello"}
print(x)
print(type(x))
y = {"name":"Sai Vardhan","Subject":"Python Full Stack"}
print(y)
print(type(y))
'''
#User Inputs
'''
1 2 3 4
100 200 100 300
{1:100,2:200,3:100,4:300}
'''
#Source Code
'''
keys = list(map(int,input().split()))
values = list(map(int,input().split()))
d = dict(zip(keys,values))
print(d)
print(type(d))
'''

#Accessing
#Indexing
'''
d = {10:100,20:200,30:300,40:400}
print(d[20])
print(d[40])
'''
#Looping
#Example - 1
'''
d = {10:100,20:200,30:300,40:400}
print("Keys :")
for i in d:
    print(i)
'''
#Example - 2
'''
d = {10:100,20:200,30:300,40:400}
print("Values: ")
for i in d:
    print(d[i])
'''
#Example - 3
'''
d = {10:100,20:200,30:300,40:400}
print("Keys and Values")
for i in d:
    print(i,d[i])
'''
#Methods
#get()
'''
d = {10:100,20:200,30:300,40:400,50:500}
print(d.get(20))
print(d.get(40))
'''
#keys()
'''
d = {10:100,20:200,30:300,40:400,50:500}
print(d.keys())
'''
#values()
'''
d = {10:100,20:200,30:300,40:400,50:500}
print(d.values())
'''
#items()
'''
d = {10:100,20:200,30:300,40:400,50:500}
print(d.items())
'''

#Diff b/w indexing and get()
'''
d = {10:100,20:200,30:300,40:400}
print(d[20])
print(d.get(20))
print(d.get(50))
print(d[50])
'''


#Problem - 1 [ Sum of values of Even Keys ]
'''
keys = list(map(int,input().split()))
values = list(map(int,input().split()))
d = dict(zip(keys,values))
temp = 0
for i in d:
    if i%2==0:
        temp = temp + d[i]
print(temp)
'''
#Problem - 2 [ Display Month Name ]
'''
months = {1:"Jauary",
          2:"Feb",
          3:"March",
          4:"April",
          5:"May",
          6:"June",
          7:"July",
          8:"August",
          9:"September",
          10:"October",
          11:"November",
          12:"December"
    }
date,month,year = map(int,input().split("-"))
print(f"Date: {date}")
print(f"Month: {months[month]}")
print(f"Year: {year}")
'''
























