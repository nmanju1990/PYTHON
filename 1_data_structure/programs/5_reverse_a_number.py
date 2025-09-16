n = int(input("enter a number:"))
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



      





