
#factors of given number
n=int(input("enter a number:"))
print(f"NEW N VALUE IS{n}")
sum=0
for x in range(1,n+1):
   if n % x == 0:
      sum=sum+x
      print(f"factors of the given number:{x}")
print(f"sum of the factors {sum}")


       
       