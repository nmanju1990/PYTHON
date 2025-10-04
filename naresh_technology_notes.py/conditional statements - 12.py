#Elif Statements
#Problem - 1
'''
Take three numbers from the user seperated with spaces
in a single line. Find the First Largest Value among
three numbers
=> 10 30 20
=> 30

=>20 5 15
=>20

=>30 35 23
=>35
'''
#Source code
'''
a,b,c = map(int,input().split())
if ((a>b) and (a>c)):
    print(a)
elif ((b>a) and (b>c)):
    print(b)
else:
    print(c)
'''
#Problem - 2
'''
Take three numbers from the user seperated with comma
in a single line. Find the Second Largest Value among
three numbers
=> 10 30 20
=> 20

=>20 5 15
=15

=>30 35 23
=>30
'''
#Source Code:
#Approach - 1
'''
a,b,c = map(int,input().split(","))
if ((a>b) and (a>c)):
    if(b>c):
        print(b)
    else:
        print(c)
elif ((b>a) and (b>c)):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if (b>a):
        print(b)
    else:
        print(a)
'''
#Approach - 2
'''
a,b,c = map(int,input().split(","))
if ((a>b) and (a>c)):
    a = 0
elif ((b>a) and (b>c)):
    b = 0
else:
    c = 0
if((a>b) and (a>c)):
    print(a)
elif ((b>a) and (b>c)):
    print(b)
else:
    print(c)
'''
#Conditional Expression
#Problem - 3
'''
Check weather the given number is Even or Odd
'''
#Approach - 1
'''
a = 13
if (a%2==0):
    print("Even")
else:
    print("Odd")
'''
#Approach - 2
'''
a = 13
result = "Even" if (a%2==0) else "Odd"
print(result)
'''
#Problem - 4
'''
Next Even Integer
'''
#Approach - 1
'''
n = int(input())
if n%2==0:
    print(n+2)
else:
    print(n+1)
'''
#Approach - 2
'''
n = int(input())
result = n+2 if n%2==0 else n+1
print(result)
'''










    
















