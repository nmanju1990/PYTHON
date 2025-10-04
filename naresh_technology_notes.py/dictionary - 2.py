#Dictionary
#Insertion
#Indexing Syntax
'''
d = {10:100,20:200,30:300}
print(d)
d[40] = 400
print(d)
'''
#Method - update()
'''
d = {10:100,20:200,30:300}
print(d)
d.update({40:400,50:500})
print(d)
'''

#Updation
#Indexing Syntax
'''
d = {10:100,20:200,30:300}
print(d)
d[20] = 250
print(d)
d[10] = 150
print(d)
'''
#Method - update()
'''
d = {10:100,20:200,30:300}
print(d)
d.update({10:150,20:250})
print(d)
'''

#Deletion
#pop()
'''
d = {10:100,20:200,30:300,40:400}
print(d)
d.pop(20)
print(d)
'''
#popitem()
'''
d = {10:100,20:200,30:300,40:400}
print(d)
d.popitem()
print(d)
'''
#clear()
'''
d = {10:100,20:200,30:300,40:400}
print(d)
d.clear()
print(d)
'''

#Built in functions
#len()
'''
d = {10:100,20:200,30:300,40:400}
print(len(d))
'''
#min()
'''
d = {10:100,20:200,30:300,40:400}
print(min(d))
'''
#max()
'''
d = {10:100,20:200,30:300,40:400}
print(max(d))
'''
#sorted()
'''
d = {20:100,30:200,400:300,100:400}
print(sorted(d))
'''


#Problem - 1 [ Frequency of elements ]
#Approach - 1
'''
n = int(input())
x = list(map(int,input().split()))
d = {}
for i in x:
    if i not in d:
        d[i] = x.count(i)
print(d)
'''
#Approach - 2
'''
n = int(input())
x = list(map(int,input().split()))
d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
'''

#Problem - 2 [ Word Frequency ( E olymp ) ]
#approach - 1
'''
d = {}
n = int(input())
for i in range(n):
    word = input()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
#print(d)
r1 = d.values()
r2 = max(r1)
#print(r2)
r3 = []
for i in d:
    if d[i] == r2:
        r3.append(i)
#print(r3)
r3.sort()
r4 = r3[-1]
#print(r4)
print(r4,r2)
'''
#Appraoch - 2
'''
d = {}
n = int(input())
for i in range(n):
    word = input()
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
#print(d)
r2 = max(d.values())
#print(r2)
r3 = [i for i in d if d[i]==r2] #List Comprehension
#print(r3)
r3.sort()
r4 = r3[-1]
#print(r4)
print(r4,r2)
'''
#Problem - 3
'''
keys=list(map(int,input().split()))
values=list(map(int,input().split()))
d=dict(zip(keys,values))
temp=0
temp1=0
for i in d:
    if i%2==0:
        temp=temp+d[i]
    if i%2!=0:
        temp1=temp1+d[i]
if (temp - temp1) > 0:
    print(temp-temp1)
else:
    print(-1 * (temp-temp1))
'''











