#Loop Control Statements
#Example - 1 [ Break ]
'''
for i in range(2,8):
    if i == 5:
        print("hello world")
        break
    print(i)
print("End of the Loop")
'''
#Example - 2 [ Break ]
'''
temp = 10
while temp >= 1:
    if temp == 5:
        print("Hello World")
        break
    print(temp)
    temp = temp - 1

print("End of loop")
'''
#Example - 3 [ Continue ]
'''
for i in range(2,8):
    if i == 5:
        print("hello world")
        continue
    print(i)
print("End of the Loop")
'''
#Example - 4 [ Continue ]
'''
temp = 10
while temp >= 1:
    if temp == 5:
        print("Hello World")
        continue
    print(temp)
    temp = temp - 1
print("End of loop")
'''
#Example - 5 [ Pass ]
'''
for i in range(10):
    pass #Maintain good Syntax, It does not do anything
'''
#Example - 6 [ Pass ]
'''
temp = 10
while temp >= 1:
    pass
    temp = temp - 1
'''
#Example - 7 [ While with else ]
'''
temp = 10
while temp >= 1:
    if temp == 5:
        break
    print(temp)
    temp = temp - 1
else:
    print("Hello World")
'''
#Example - 8 [ For with else ]
'''
for x in range(1,11):
    if x == 5:
        break
    print(x)
else:
    print("Hello Python")
'''
#Problem - 1
'''
Find Reverese of the number using control statements, conditional
statements and operators.
=>123
=>321

=>100
=>1

=>-123
=>-321

=>-100
=>-1

=>0
=>0
'''
#Source Code
'''
n = int(input("Enter a number: "))
res = 0
if n >= 0:
    while n > 0:
        rem = n % 10
        res = (res * 10) + rem
        n = n // 10
else:
    n = -1 * n
    while n > 0:
        rem = n % 10
        res = (res * 10) + rem
        n = n // 10
    res = -1 * res
print(res)
'''










