n=int(input("enter a number:"))
print(n//10)
n=n%100
print(n//10)
n=n%10
print(n)




n=int(input("enter a number:"))
temp=0
while n>0:
    rem=n%10
    temp=(temp*10)+rem
    n=n//10
    print(temp)
while temp>0:
     print(temp%10)
     temp=temp//10          



      