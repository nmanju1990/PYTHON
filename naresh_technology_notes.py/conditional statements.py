#conditional Statements
#If - Statement
'''
a = 10
b = 10
if a == b:
    print("The a is equals to b")
    print("Hello world")
print("End of The If statement")
'''
#Problem - 1
#Print "Even" If the Number is Even
'''
n = int(input("Enter a number: "))
if n%2==0:
    print("Even")
print("End of the Program")
'''
#Problem  - 2
#Take a word from the user, Print yes if there is vowel in
#string
#Test Cases:
#T - 1
'''
=>hello
=>Yes
'''
#T - 2
'''
=>xyz
'''
#Edge Case:
'''
=>Abc
=>Yes
'''
'''
n = input("Enter a String/word: ")
if (("a" in n) or ("e" in n) or ("i" in n) or ("o" in n) or ("u" in n)):
    print("Yes")
'''
#Problem - 3
'''
Take a single character from the users, Print Yes if it is
a consonant
'''
#Source Code
'''
n = input("Enter a character: ")
if ((n!="a")and(n!="e")and(n!="i")and(n!="o")and(n!="u")):
    print("Yes")
'''
#If - Else
#Problem  - 1
'''
Take an integer input from the user, Print "+ve" if the
number is Positive, otherwise print "-ve"
'''
#source Code
#Approach - 1
'''
n = int(input("Enter a number: "))
if (n>0):
    print("+ve")
else:
    print("-ve")
'''
#Approach - 2
'''
n = int(input("Enter a number: "))
if (n<0):
    print("-ve")
else:
    print("+ve")
'''
#Problem - 2
'''
Ask user to enter age and checlk if they can vote or not
Condtion: age is greater than or equals to 18
If user can vote => display "Can Vote"
If user can not Vote => Display "Can not Vote"
'''
#Source code:
#Approach - 1
'''
n = int(input("Enter  your age: "))
if (n>=18):
    print("Can vote")
else:
    print("Can not vote")
'''
#Approach - 2
'''
n = int(input("Enter  your age: "))
if (n<18):
    print("Can not vote")
else:
    print("Can vote")
'''
#Problem  - 3 [ Triangle Validator ]
'''
a,b,c = map(int,input().split())
if ((a+b>c) and (b+c>a) and (a+c>b)):
    print("Yes")
else:
    print("No")
'''













    
