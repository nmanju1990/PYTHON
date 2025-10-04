#Built in Function
#len()
'''
a = "hello"
print(len(a))
b = "abc"
print(len(b))
x = "hello world"
print(len(x))
'''
#min()
'''
x1 = "abc"
print(min(x1))
x2 = "123"
print(min(x2))
x3 = "ABC"
print(min(x3))
x4 = "abcABC"
print(min(x4))
'''
#max()
'''
x1 = "abc"
print(max(x1))
x2 = "123"
print(max(x2))
x3 = "ABC"
print(max(x3))
x4 = "abcABC"
print(max(x4))
'''
#Problem - 1 [ Find length of last word ]
#Approach - 1
'''
s = input()
#print(s)
s = s.strip()
#print(s)
s = s[::-1]
#print(s)
temp = 0
for i in s:
    if i != " ":
        temp = temp + 1
    else:
        print(temp)
        break
'''
#Approach - 2
'''
s = input()
#print(s)
s = s.strip()
#print(s)
x = s.split()
#print(x)
#print(x[-1])
print(len(x[-1]))
'''

#Problem - 2 [ Reverse the vowels of the string ]
'''
s = input()
#print(s)
vowels = "aeiouAEIOU" #Creation
x = "" #creation
for i in s: #Accessing
    if i in vowels: #External Operation [membership]
        x = x + i #External Operation [Concatenation]
#print(s)
#print(x)
temp = "" #Creation
for i in s: #Accesing
    if i in vowels: ##External Operation [membership]
        temp = temp + x[-1] ##External Operation [Concatenation] + Accessing
        x = x[:len(x)-1] #Builtin functions, Slicing
    else:
        temp = temp + i #Concatenation
print(temp)
'''
#Problem - 3 [ Way too Long Words ]
'''
n = int(input())
for i in range(n):
    s = input()
    if len(s) > 10:
        print(s[0] + str(len(s)-2) + s[-1])
    else:
        print(s)
'''






















