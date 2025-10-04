#Pattenrs
#Problem - 1 [ Combination Patterns ] [ Complete Pattern ]
'''
n = 5
# # # # #
* * * * *
# # # # #
* * * * *
# # # # #
'''
#Source code
#Approach - 1 [ Nested Loops ]
'''
n = 5
for i in range(n):
    if i%2==0:
        for j in range(n):
            print("#",end=" ")
    else:
        for j in range(n):
            print("*",end=" ")
    print()
'''
#Approach - 2 [ String Repetetion ]
'''
n = 5
for i in range(n):
    if i%2==0:
        print("# "*n)
    else:
        print("* "*n)
'''
#Problem - 2 [ Symbolic Pattenrn ] [ In complete Pattern ]
'''
n = 5
#
# #
# # #
# # # #
# # # # #
'''
#Source code
#Approach - 1 [ Nested Loops ] [With conditions]
'''
n = 10
for i in range(n):
    for j in range(n):
        if i>=j:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Approach - 2 [ Nested Loops ] [ Without Conditions ]
'''
i = 0 | j = 1
i = 1 | j = 2
i = 2 | j = 3
i = 3 | j = 4
i = 4 | j = 5
'''
'''
n = 5
for i in range(n):
    for j in range(i+1):
        print("#",end=" ")
    print()
'''
#Approach - 3 [ Only One Loop ] [ Effiecient Approach ]
'''
n = 5
for i in range(n):
    print("# "*(i+1))
'''
#Numeric Patterns
#Problem - 1 [ Complete Pattern ]
'''
n = 3
1 1 1
2 2 2
3 3 3
'''
#Source Code:
#Approach - 1 [ Nested Loops ] [ Temp Varibale ]
'''
temp = 1
n = 3
for i in range(n):
    for j in range(n):
        print(f"{temp}",end=" ")
    print()
    temp = temp + 1
'''
#Approach - 2 [ Nested Loops ] [ Without Temp Variable ]
'''
n = 3
for i in range(n):
    for j in range(n):
        print(f"{i+1}",end=" ")
    print()
'''
#Problem - 2
'''
n = 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
#Source code:
#Approach - 1 [ Nested Loops ] [ Temp Varibale ]
'''
n = 3
for i in range(n):
    temp = 1
    for j in range(n):
        print(f"{temp}",end=" ")
        temp = temp + 1
    print()
'''
#Approach - 2 [ Nested Loops ] [ Without Temp Variable ]
'''
n = 3
for i in range(n):
    for j in range(n):
        print(f"{j+1}",end=" ")
    print()
'''
#Problem - 3 [ Complete ] 
'''
n = 4
2 2 2 2
4 4 4 4
6 6 6 6
8 8 8 8
'''
#Source Code:
'''
n = 4
temp = 2
for i in range(n):
    for j in range(n):
        print(f"{temp}",end=" ")
    print()
    temp = temp + 2
'''
#Problem - 4 [ Incomplete ]
'''
n = 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
#Source Code:
#Approach - 1 [ Nested Loops ] [With conditions]
'''
n = 5
for i in range(n):
    temp = 1
    for j in range(n):
        if i>=j:
            print(f"{temp}",end=" ")
        temp = temp + 1
    print()
'''
#Approach - 2 [ Nested Loops ] [ Without Conditions ]
'''
n = 5
for i in range(n):
    temp = 1
    for j in range(i+1):
        print(f"{temp}",end=" ")
        temp = temp + 1
    print()
'''
#Problem - 5 [ Incomplete ] [combination]
'''
n = 5
1
# #
2 2 2
# # # #
3 3 3 3 3
'''
#Source code:
'''
n = 5
temp = 1
for i in range(n):
    if i%2==0:
        for j in range(n):
            if i>=j:
                print(f"{temp}",end=" ")
        temp = temp + 1
    else:
        for j in range(n):
            if i>=j:
                print(f"#",end=" ")
    print()
'''
#Problem - 6 [ Incomplete ] [combination]
'''
n = 5
1
# #
1 2 3
# # # #
1 2 3 4 5
'''
#Source Code:
'''
n = 5
for i in range(n):
    if i%2==0:
        temp = 1
        for j in range(n):
            if i>=j:
                print(f"{temp}",end=" ")
            temp = temp + 1
    else:
        for j in range(n):
            if i>=j:
                print(f"#",end=" ")
    print()
'''
#Example Patterns
#Pattern - 1
'''
n = 5
# # # # #
# # # #
# # #
# #
#
'''
#Pattern - 2
'''
n = 5
# # # # #
  # # # #
    # # #
      # #
        #
'''
#Pattern - 3
'''
n = 4
    #
   # #
  # # #
 # # # #
# # # # #
'''
#Pattern - 4
'''
n = 5
#
# #
# # #
# # # #
# # # # #
# # # #
# # #
# #
#
'''
#Pattern = 5
'''
n = 4
# # # #
#     #
#     #
# # # #
n = 5
$ $ $ $ $
$       $
$       $
$       $
$ $ $ $ $
'''



























        
    







