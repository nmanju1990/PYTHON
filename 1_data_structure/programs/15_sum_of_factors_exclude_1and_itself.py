# sum of the factors of given number and excluding 1 and itself
temp=0
n=int(input("enter a number:"))
for x in range (2,n):
    if n % x == 0:
       temp =temp+x
       print(temp)
