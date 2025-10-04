#Looping Statements / Control statements
#Problem - 1
'''
Given an integer find the factors of given integer
including 1 and itself

=>12
=>1 2 3 4 6 12


=>21
=>1 2 7 21

=>8
=>1 2 4 8
'''
#Source Code
'''
n = int(input("Enter a number: "))
for x in range(1,n+1):
    if n%x==0:
        print(x,end=" ")
'''
#Problem - 2
'''
Given an integer as in input from the user, find sum of
factors of a given number excluding 1 and itself.

=>8
=>6

=>21
=>9
'''
#Source Code
'''
n = int(input("Enter a number: "))
temp = 0
for x in range(2,n):
    if n%x==0:
        temp = temp + x
print(temp)
'''
#Problem - 3
'''
Given a integer input from the user, check weather the given
number is Prime or not ?
if it is prime, Dispaly "Prime Number", if it is not prime,
Display "Not a Prime Number".
'''
#Source Code
#Approach - 1
'''
n = int(input("Enter a number: "))
temp = 0
for x in range(1,n+1):
    if n%x==0:
        temp = temp + 1
if temp == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
'''
#Approach - 2
'''
n = int(input("Enter a number: "))
temp = 0
for x in range(2,n):
    if n%x==0:
        temp = temp + 1
if temp == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
'''
#Approach - 3
'''
n = int(input("Enter a number: "))
for i in range(2,n):
    if n%i == 0:
        print("Not a Prime Number")
        break
else: #For Loop
    print("Prime Number")
'''
#Problem - 4 [ Fever from Codechef ]
#Approach - 1 [For Loop]
'''
t = int(input())
for i in range(t):
    x = int(input())
    if x > 98:
        print("YES")
    else:
        print("NO")
'''
#Approach - 2 [ while Loop ]
'''
t = int(input())
while (t>0):
    x = int(input())
    if x > 98:
        print("YES")
    else:
        print("NO")
    t = t - 1
'''
#Problem - 5 [ Decomposition of three digit number fom Eolymp]
#Approach - 1
'''
n = int(input())
if n < 0:
    n = -1 * n
print(n//100)
n = n%100
print(n//10)
n = n%10
print(n)
'''
#Approach - 2
'''
n = int(input())
if n < 0:
    n = -1 * n
temp = 0
while n > 0:
    rem = n%10
    temp = (temp * 10) + rem
    n = n // 10
while temp > 0:
    print(temp%10)
    temp = temp // 10
'''
    
    


















