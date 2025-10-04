#Match Case
#Example - 1
'''
1 -> Monday
2 -> Tuesday
3 -> Wed
4 -> thu
5 -> Friday
6 -> Sat
7 -> Sun
'''
#Approach - 1
'''
option = int(input("Enter a number: "))
match option:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input")
'''
#Approach - 2
'''
option = int(input("Enter A number: "))
if (option == 1):
    print("Monday")
elif (option == 2):
    print("Tuesday")
elif (option == 3):
    print("Wednesday")
elif (option == 4):
    print("Thursday")
elif (option == 5):
    print("Friday")
elif (option == 6):
    print("Saturday")
elif (option == 7):
    print("Sunday")
else:
    print("Invalid Input")
'''
#Program - 1
#Maximum Pizzas
'''
n,x = map(int,input().split())
trs = n*x

if trs%4==0:
    print(trs//4)
else:
    print((trs//4)+1)
'''
#Problem - 2 [ Watermelon ]
'''
w = int(input())
if (w>2 and w%2==0): #Relational,logical,Arithemetic
    print("YES")
else:
    print("NO")
'''
#Problem - 3 [ ATM ]
#Appraoch - 1
'''
x,y = map(float,input().split())
if (x%5!=0):
    print("{:.2f}".format(y))
else:
    if (x+0.50 <= y):
        print("{:.2f}".format(y-(x+0.50)))
    else:
        print("{:.2f}".format(y))
'''
#Approach - 2
'''
x,y = map(float,input().split())
if (x%5==0 and (x+0.50 <= y)):
    print("{:.2f}".format(y-(x+0.50)))
else:
    print("{:.2f}".format(y))
'''
#Program - 4 [ Second largest among 3 numbers ]
a,b,c = map(int,input().split())
if (a>b and a>c):
    a = 0
elif (b>a and b>c):
    b = 0
else:
    c = 0
if (a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else:
    print(c)




















        
